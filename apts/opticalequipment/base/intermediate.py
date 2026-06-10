from .equipment import OpticalEquipment


class IntermediateOpticalEquipment(OpticalEquipment):
    """
    Base class for intermediate optical equipment like Barlows, Diagonals, Filters, etc.
    """

    def __init__(
        self,
        vendor,
        optical_length=0.0,
        mass=0.0,
        in_connection=None,
        out_connection=None,
        # Legacy arguments for backward compatibility
        in_connection_type=None,
        out_connection_type=None,
        in_gender=None,
        out_gender=None,
        inputs=None,
        outputs=None,
    ):
        # Merge legacy arguments into new ones
        if in_connection is None:
            if in_connection_type is not None:
                in_connection = (in_connection_type, in_gender)
        if out_connection is None:
            if out_connection_type is not None:
                out_connection = (out_connection_type, out_gender)

        super().__init__(
            focal_length=0.0,
            vendor=vendor,
            optical_length=optical_length,
            mass=mass,
            inputs=inputs,
            outputs=outputs,
        )

        if in_connection:
            if isinstance(in_connection, tuple):
                self.add_input(*in_connection)
            else:
                self.add_input(in_connection)

        if out_connection:
            if isinstance(out_connection, tuple):
                self.add_output(*out_connection)
            else:
                self.add_output(out_connection)

    @property
    def in_connection_type(self):
        return self._inputs[0][0] if self._inputs else None

    @property
    def in_gender(self):
        return self._inputs[0][1] if self._inputs else None

    @property
    def out_connection_type(self):
        return self._outputs[0][0] if self._outputs else None

    @property
    def out_gender(self):
        return self._outputs[0][1] if self._outputs else None
