import tkinter as tk
from tkinter import messagebox, ttk

from backend import ALGORITHMS, generate_numbers, run_sort


class SortApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Sorting")
        self.resizable(False, False)
        self._build()

    def _build(self) -> None:
        pad = {"padx": 6, "pady": 4}
        root = ttk.Frame(self, padding=10)
        root.grid()

        inp = ttk.LabelFrame(root, text="Numbers", padding=8)
        inp.grid(row=0, column=0, sticky="ew", **pad)

        ttk.Label(inp, text="Numbers (separated by spaces or commas):").grid(row=0, column=0, columnspan=4, sticky="w")
        self.numbers_var = tk.StringVar()
        ttk.Entry(inp, textvariable=self.numbers_var, width=50).grid(row=1, column=0, columnspan=4, sticky="ew", pady=(0, 8))

        ttk.Label(inp, text="Count:").grid(row=2, column=0, sticky="e")
        self.count_var = tk.StringVar(value="10")
        ttk.Entry(inp, textvariable=self.count_var, width=6).grid(row=2, column=1, sticky="w")
        ttk.Label(inp, text="From:").grid(row=2, column=2, sticky="e")
        self.low_var = tk.StringVar(value="0")
        ttk.Entry(inp, textvariable=self.low_var, width=6).grid(row=2, column=3, sticky="w")
        ttk.Label(inp, text="To:").grid(row=3, column=2, sticky="e")
        self.high_var = tk.StringVar(value="100")
        ttk.Entry(inp, textvariable=self.high_var, width=6).grid(row=3, column=3, sticky="w")
        ttk.Button(inp, text="Generate random", command=self.on_generate).grid(row=3, column=0, columnspan=2, sticky="w")

        alg = ttk.LabelFrame(root, text="Algorithm", padding=8)
        alg.grid(row=1, column=0, sticky="ew", **pad)
        self.algorithm_var = tk.StringVar(value=next(iter(ALGORITHMS)))
        for name in ALGORITHMS:
            ttk.Radiobutton(alg, text=name, value=name, variable=self.algorithm_var).pack(side="left", padx=4)
        ttk.Button(alg, text="Sort", command=self.on_sort).pack(side="right")

        out = ttk.LabelFrame(root, text="Result", padding=8)
        out.grid(row=2, column=0, sticky="ew", **pad)
        self.time_var = tk.StringVar(value="")
        ttk.Label(out, textvariable=self.time_var).grid(row=0, column=0, sticky="w")
        self.output = tk.Text(out, height=6, width=50, wrap="word", state="disabled")
        self.output.grid(row=1, column=0, sticky="ew")

    def _parse_numbers(self) -> list[int]:
        raw = self.numbers_var.get().replace(",", " ").split()
        try:
            return [int(x) for x in raw]
        except ValueError as e:
            raise ValueError(f"Invalid number: {e.args[0].split(': ')[-1]}") from None

    def _set_output(self, text: str) -> None:
        self.output.configure(state="normal")
        self.output.delete("1.0", "end")
        self.output.insert("1.0", text)
        self.output.configure(state="disabled")

    def on_generate(self) -> None:
        try:
            count = int(self.count_var.get())
            low = int(self.low_var.get())
            high = int(self.high_var.get())
            nums = generate_numbers(count, low, high)
        except ValueError as e:
            messagebox.showerror("Invalid input", str(e))
            return
        self.numbers_var.set(" ".join(map(str, nums)))

    def on_sort(self) -> None:
        try:
            nums = self._parse_numbers()
        except ValueError as e:
            messagebox.showerror("Invalid input", str(e))
            return
        if not nums:
            messagebox.showwarning("No numbers", "Enter some numbers or generate random ones first.")
            return
        result = run_sort(self.algorithm_var.get(), nums)
        self.time_var.set(f"{result.algorithm}: sorted {len(nums)} numbers in {result.seconds:.4f} s")
        self._set_output(" ".join(map(str, result.numbers)))


def main() -> None:
    SortApp().mainloop()


if __name__ == "__main__":
    main()
