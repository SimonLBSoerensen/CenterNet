class CSVLoggerDL:
    def __init__(self, file_out="hist.csv", epoch_label="epoch"):
        self.file_out = file_out
        self.header_written = False
        self.epoch = 0
        self.epoch_label = epoch_label

    def _write_values(self, values, write_mode="a"):
        with open(self.file_out, write_mode) as f:
            for v in values[:-1]:
                f.write(f"{v},")
            f.write(f"{values[-1]}\n")

    def add(self, value_dict, epoch=None):
        if epoch is None and self.epoch_label not in value_dict:
            value_dict[self.epoch_label] = self.epoch
            self.epoch += 1
        elif epoch:
            value_dict[self.epoch_label] = epoch

        if not self.header_written:
            if self.epoch_label in value_dict:
                self.header = [self.epoch_label]
                self.header += [el for el in list(value_dict.keys()) if el != self.epoch_label]
            else:
                self.header = list(value_dict.keys())

            self._write_values(values=self.header, write_mode="w")
            self.header_written = True

        values = []
        for h in self.header:
            value = value_dict[h] if h in value_dict else ""
            values.append(value)
        self._write_values(values=values, write_mode="a")
