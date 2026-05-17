from typing import TYPE_CHECKING, Optional

from .engine import PolarAlignment

if TYPE_CHECKING:
    pass


class PolarAlignmentWizard:
    PHASE_SELECT_STAR = "SELECT_STAR"
    PHASE_ROTATION = "ROTATION"
    PHASE_ADJUSTMENT = "ADJUSTMENT"

    def __init__(self, observation):
        self.observation = observation
        self.pa: Optional[PolarAlignment] = None
        self.phase = self.PHASE_SELECT_STAR
        self.error = None
        self.instructions = "Please select a target star for polar alignment."

    def select_star(self, star_name):
        self.pa = PolarAlignment(self.observation, target_star_name=star_name)
        self.phase = self.PHASE_ROTATION
        self.instructions = "Take the first frame at the home position (RA=0)."

    def add_rotation_frame(self, filepath, ra_rotation_deg):
        if self.phase != self.PHASE_ROTATION:
            raise ValueError(f"Not in rotation phase. Current phase: {self.phase}")
        assert self.pa is not None
        success = self.pa.add_frame(
            filepath, ra_rotation_deg=ra_rotation_deg, phase="rotation"
        )
        if success:
            if len(self.pa.rotation_frames) == 1:
                self.instructions = (
                    "Rotate RA (e.g. 60-90 degrees) and take another frame."
                )
            elif len(self.pa.rotation_frames) >= 2:
                self.instructions = "Rotation data collected. You can add more frames or calculate the alignment."
        return success

    def calculate(self):
        assert self.pa is not None
        if self.pa is None or len(self.pa.rotation_frames) < 2:
            raise ValueError("Need at least 2 rotation frames to calculate alignment.")
        correction = self.pa.calculate_correction()
        if correction:
            self.error = correction["error_arcmin"]
            self.instructions = (
                f"Alignment calculated. Error: {self.error:.1f}'. "
                f"{correction['instructions']}. Start adjustment phase for live feedback."
            )
            return correction
        return None

    def start_adjustment(self):
        assert self.pa is not None
        if self.pa is None or self.pa.mount_axis_image is None:
            # Try to calculate if not done yet
            self.calculate()
        self.phase = self.PHASE_ADJUSTMENT
        self.instructions = (
            "Take adjustment frames for live feedback. "
            "Adjust Altitude and Azimuth knobs as instructed."
        )

    def add_adjustment_frame(self, filepath):
        if self.phase != self.PHASE_ADJUSTMENT:
            raise ValueError(f"Not in adjustment phase. Current phase: {self.phase}")
        assert self.pa is not None
        success = self.pa.add_frame(filepath, phase="adjustment")
        if success:
            correction = self.pa.calculate_correction()
            if correction:
                self.error = correction["error_arcmin"]
                self.instructions = (
                    f"Error: {self.error:.1f}'. {correction['instructions']}"
                )
                return correction
        return None

    def get_status(self):
        return {
            "phase": self.phase,
            "error_arcmin": self.error,
            "instructions": self.instructions,
            "target_star": self.pa.target_star_name if self.pa else None,
            "rotation_frames_count": len(self.pa.rotation_frames) if self.pa else 0,
            "adjustment_frames_count": len(self.pa.adjustment_frames) if self.pa else 0,
        }
