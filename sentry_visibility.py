import math
import tkinter as tk

EPS = 1e-9


# ===== GEOMETRY FUNCTIONS =====

def seg_intersect_ray(seg_a, seg_b, ray_origin, ray_dir):
    ox, oy = ray_origin
    dx, dy = ray_dir
    x1, y1 = seg_a
    x2, y2 = seg_b
    rx, ry = x2 - x1, y2 - y1
    denom = dx * ry - dy * rx
    if abs(denom) < EPS:
        return None
    t = ((x1 - ox) * ry - (y1 - oy) * rx) / denom
    u = ((x1 - ox) * dy - (y1 - oy) * dx) / denom
    if t >= -EPS and -EPS <= u <= 1 + EPS:
        return t, u
    return None


def make_unit_vector(theta):
    return math.cos(theta), math.sin(theta)


def cast_ray(ray_origin, ray_dir, segments):
    nearest_t = float('inf')
    for (a, b) in segments:
        r = seg_intersect_ray(a, b, ray_origin, ray_dir)
        if r:
            t, _ = r
            if t > EPS and t < nearest_t:
                nearest_t = t
    return nearest_t if nearest_t < float('inf') else None


def can_sentry_see_outside(sentry, segments, step_deg=3):
    sx, sy = sentry
    for th in range(0, 360, step_deg):
        theta = math.radians(th)
        dir_vec = make_unit_vector(theta)
        t = cast_ray((sx, sy), dir_vec, segments)
        if t is None:
            return True
    return False


# ===== GUI APPLICATION =====

class CoordinateApp:
    def __init__(self, master):
        self.master = master
        master.title("Sentry Visibility - Coordinate Plane")

        self.width, self.height = 800, 600
        self.scale = 40  # 1 coordinate unit = 40 pixels
        self.origin = (self.width // 2, self.height // 2)

        # Canvas setup
        self.canvas = tk.Canvas(master, width=self.width, height=self.height, bg='white')
        self.canvas.pack(pady=10)
        self.draw_axes()

        # Control panel
        frm = tk.Frame(master)
        frm.pack()

        # Inputs for segment
        tk.Label(frm, text="Segment (x1,y1)-(x2,y2):").grid(row=0, column=0)
        self.seg_x1 = tk.Entry(frm, width=4)
        self.seg_y1 = tk.Entry(frm, width=4)
        self.seg_x2 = tk.Entry(frm, width=4)
        self.seg_y2 = tk.Entry(frm, width=4)
        self.seg_x1.grid(row=0, column=1)
        self.seg_y1.grid(row=0, column=2)
        self.seg_x2.grid(row=0, column=3)
        self.seg_y2.grid(row=0, column=4)
        tk.Button(frm, text="Add Segment", command=self.add_segment).grid(row=0, column=5, padx=5)

        # Inputs for sentry
        tk.Label(frm, text="Sentry (x,y):").grid(row=1, column=0)
        self.sx = tk.Entry(frm, width=4)
        self.sy = tk.Entry(frm, width=4)
        self.sx.grid(row=1, column=1)
        self.sy.grid(row=1, column=2)
        tk.Button(frm, text="Add Sentry", command=self.add_sentry).grid(row=1, column=3, padx=5)

        tk.Button(frm, text="Check Visibility", command=self.check_visibility).grid(row=1, column=4, padx=5)
        tk.Button(frm, text="Clear", command=self.clear).grid(row=1, column=5, padx=5)

        self.segments = []
        self.sentries = []

    def to_canvas(self, x, y):
        cx, cy = self.origin
        return cx + x * self.scale, cy - y * self.scale

    def draw_axes(self):
        cx, cy = self.origin
        self.canvas.create_line(0, cy, self.width, cy, fill='gray', width=1)
        self.canvas.create_line(cx, 0, cx, self.height, fill='gray', width=1)
        for i in range(-10, 11):
            x, y = self.to_canvas(i, 0)
            self.canvas.create_line(x, cy - 3, x, cy + 3, fill='gray')
            if i != 0:
                self.canvas.create_text(x, cy + 12, text=str(i), fill='black')
        for j in range(-7, 8):
            x, y = self.to_canvas(0, j)
            self.canvas.create_line(cx - 3, y, cx + 3, y, fill='gray')
            if j != 0:
                self.canvas.create_text(cx - 15, y, text=str(j), fill='black')

    def add_segment(self):
        try:
            x1, y1 = float(self.seg_x1.get()), float(self.seg_y1.get())
            x2, y2 = float(self.seg_x2.get()), float(self.seg_y2.get())
            a, b = self.to_canvas(x1, y1), self.to_canvas(x2, y2)
            self.canvas.create_line(a[0], a[1], b[0], b[1], width=2, fill='blue')
            self.segments.append(((x1, y1), (x2, y2)))
        except ValueError:
            print("Invalid segment input")

    def add_sentry(self):
        try:
            sx, sy = float(self.sx.get()), float(self.sy.get())
            cx, cy = self.to_canvas(sx, sy)
            r = 5
            self.canvas.create_oval(cx - r, cy - r, cx + r, cy + r, fill='red')
            self.sentries.append((sx, sy))
        except ValueError:
            print("Invalid sentry input")

    def check_visibility(self):
        self.canvas.delete('result')
        for s in self.sentries:
            can_see = can_sentry_see_outside(s, self.segments)
            cx, cy = self.to_canvas(s[0], s[1])
            if can_see:
                self.canvas.create_text(cx, cy - 10, text='OUT', fill='green', font=('Arial', 10, 'bold'), tags='result')
            else:
                self.canvas.create_text(cx, cy - 10, text='IN', fill='red', font=('Arial', 10, 'bold'), tags='result')
                self.canvas.create_oval(cx - 8, cy - 8, cx + 8, cy + 8, outline='red', width=2, tags='result')

    def clear(self):
        self.canvas.delete("all")
        self.segments.clear()
        self.sentries.clear()
        self.draw_axes()


if __name__ == "__main__":
    root = tk.Tk()
    app = CoordinateApp(root)
    root.mainloop()
