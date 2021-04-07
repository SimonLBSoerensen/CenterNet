class CSVLoggerDL:
    def __init__(self, file_out="hist.csv", auto_epochs=True):
        self.file_out = file_out
        self.header_written = False
        self.auto_epochs = auto_epochs
        self.epoch = 0
        self.epoch_name = "epoch"

    def _write_values(self, values, write_mode="a"):
        with open(self.file_out, write_mode) as f:
            for v in values[:-1]:
                f.write(f"{v},")
            f.write(f"{values[-1]}\n")

    def add(self, value_dict):
        if self.auto_epochs and self.epoch_name not in value_dict:
            value_dict[self.epoch_name] = self.epoch
            self.epoch += 1

        if not self.header_written:
            if self.epoch_name in value_dict:
                self.header = [self.epoch_name]
                self.header += [el for el in list(value_dict.keys()) if el != self.epoch_name]
            else:
                self.header = list(value_dict.keys())

            self._write_values(values=self.header, write_mode="w")
            self.header_written = True

        values = []
        for h in self.header:
            value = value_dict[h] if h in value_dict else ""
            values.append(value)
        self._write_values(values=values, write_mode="a")
 
