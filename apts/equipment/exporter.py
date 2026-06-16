import logging
from typing import Optional

import numpy
import pandas as pd

from ..constants import EquipmentTableLabels, GraphConstants, OpticalType
from ..i18n import gettext_, language_context
from ..opticalequipment import NakedEye
from ..optics import OpticalPath

logger = logging.getLogger(__name__)


class EquipmentExporter:
    """
    Handles the generation of tabular data from the equipment graph.
    """

    def __init__(self, equipment):
        self.equipment = equipment

    def data(self, language: Optional[str] = None) -> pd.DataFrame:
        with language_context(language):
            result = self._generate_data()
            # Translate Type column using vectorized mapping
            unique_types = result[EquipmentTableLabels.TYPE].unique()
            translation_map = {
                t: (gettext_(t.name) if isinstance(t, OpticalType) else t)
                for t in unique_types
            }
            result[EquipmentTableLabels.TYPE] = result[EquipmentTableLabels.TYPE].map(
                translation_map.get
            )

            # Remove internal columns
            if EquipmentTableLabels.IS_NAKED_EYE in result.columns:
                result = result.drop(columns=[EquipmentTableLabels.IS_NAKED_EYE])
        return result

    def _generate_data(self) -> pd.DataFrame:
        columns = [
            EquipmentTableLabels.LABEL,
            EquipmentTableLabels.TYPE,
            EquipmentTableLabels.ZOOM,
            EquipmentTableLabels.USEFUL_ZOOM,
            EquipmentTableLabels.FOV,
            EquipmentTableLabels.FOV_W,
            EquipmentTableLabels.FOV_H,
            EquipmentTableLabels.FOV_D,
            EquipmentTableLabels.EXIT_PUPIL,
            EquipmentTableLabels.DAWES_LIMIT,
            EquipmentTableLabels.RAYLEIGH_LIMIT,
            EquipmentTableLabels.IDEAL_PLANETARY_FOCAL_RATIO,
            EquipmentTableLabels.RANGE,
            EquipmentTableLabels.BRIGHTNESS,
            EquipmentTableLabels.ELEMENTS,
            EquipmentTableLabels.COMPONENTS,
            EquipmentTableLabels.FLIPPED_HORIZONTALLY,
            EquipmentTableLabels.FLIPPED_VERTICALLY,
            EquipmentTableLabels.PIXEL_SCALE,
            EquipmentTableLabels.SAMPLING,
            EquipmentTableLabels.NPF_RULE,
            EquipmentTableLabels.RULE_OF_500,
            EquipmentTableLabels.CRITICAL_FOCUS_ZONE,
            EquipmentTableLabels.BACKFOCUS_GAP,
            EquipmentTableLabels.TOTAL_MASS,
            EquipmentTableLabels.IS_NAKED_EYE,
        ]

        # Get unique paths from both visual and image outputs in a single pass
        # Access private method of equipment
        all_paths = self.equipment._get_paths(
            [GraphConstants.EYE_ID, GraphConstants.IMAGE_ID]
        )

        rows = [self._extract_path_row(path) for path in all_paths]
        result = pd.DataFrame(columns=columns)  # pyright: ignore
        result = self._merge_path_data(result, rows, columns)

        # Add ID column as first
        if not result.empty:
            result["ID"] = result.index
            result = result[["ID"] + columns]
        else:
            result["ID"] = []
            result = result[["ID"] + columns]

        return result  # pyright: ignore

    def _extract_path_row(self, path: OpticalPath) -> list:
        """
        Extract technical parameters for a single optical path.
        """
        # Determine if the main optic is Binoculars or NakedEye
        is_naked_eye = isinstance(path.telescope, NakedEye)

        # Calculate useful_zoom
        useful_zoom_value = path.is_magnification_useful()

        # Get output type
        output_type_value = path.output.output_type()

        # Calculate Exit Pupil
        exit_pupil_value = path.exit_pupil().to("mm").magnitude
        if exit_pupil_value < 0:
            exit_pupil_value = 0

        flipped_horizontally, flipped_vertically = path.get_image_orientation()

        # Pixel Scale
        pixel_scale_value = path.pixel_scale()
        pixel_scale_magnitude = (
            pixel_scale_value.magnitude if pixel_scale_value is not None else numpy.nan
        )

        # NPF Rule
        npf_value = path.npf_rule()
        npf_magnitude = npf_value.magnitude if npf_value is not None else numpy.nan

        # Rule of 500
        r500_value = path.rule_of_500()
        r500_magnitude = r500_value.magnitude if r500_value is not None else numpy.nan

        # Sampling status (default seeing 2.0")
        sampling_value = path.sampling_status(seeing=2.0)

        # Critical Focus Zone
        cfz_value = path.critical_focus_zone()
        cfz_magnitude = cfz_value.magnitude if cfz_value is not None else numpy.nan

        # Backfocus Gap
        bf_gap_value = path.backfocus_gap()
        bf_gap_magnitude = (
            bf_gap_value.to("mm").magnitude if bf_gap_value is not None else numpy.nan
        )

        # Total Mass
        total_mass_value = path.total_mass()
        total_mass_magnitude = total_mass_value.to("gram").magnitude

        dawes = path.dawes_limit()
        rayleigh = path.rayleigh_limit()

        return [
            path.label(),
            output_type_value,
            path.zoom().magnitude,
            useful_zoom_value,
            path.fov().magnitude,
            path.fov_width().magnitude,
            path.fov_height().magnitude,
            path.fov_diagonal().magnitude,
            exit_pupil_value,
            dawes.magnitude if dawes is not None else numpy.nan,
            rayleigh.magnitude if rayleigh is not None else numpy.nan,
            path.ideal_planetary_focal_ratio() or numpy.nan,
            path.telescope.limiting_magnitude(),
            path.brightness().magnitude,
            path.length(),
            path.component_list(),
            flipped_horizontally,
            flipped_vertically,
            pixel_scale_magnitude,
            sampling_value,
            npf_magnitude,
            r500_magnitude,
            cfz_magnitude,
            bf_gap_magnitude,
            total_mass_magnitude,
            is_naked_eye,
        ]

    def _merge_path_data(
        self, result_data: pd.DataFrame, rows: list, columns: list
    ) -> pd.DataFrame:
        """
        Merge extracted rows into a DataFrame and align dtypes.
        """
        if not rows:
            return result_data

        new_data = pd.DataFrame(rows, columns=columns)  # pyright: ignore
        if result_data.empty:
            return new_data

        for col in result_data.columns:
            if result_data[col].dtype != new_data[col].dtype:
                try:
                    new_data[col] = new_data[col].astype(result_data[col].dtype)
                except Exception as e:
                    logger.warning(
                        f"Could not align dtype for column {col}: {e}. This might lead to concat issues."
                    )
        return pd.concat([result_data, new_data], ignore_index=True)  # pyright: ignore
