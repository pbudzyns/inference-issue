class DataSource:
    def get(self, name):
        return [0, 0, 0, 0]


class Plot:
    def __init__(self, *args, **kwargs):
        self.data = []

    def append(self, d):
        self.data.append(d)

    def reset_figure(self, *args, **kwargs):
        pass

    def update_figure(self):
        pass

    def compute_initial_figure(self):
        pass


class Button:
    def __init__(self, *args, **kwargs):
        pass

    def connect(self):
        pass

    def toggle(self):
        pass


class Layout:
    def addWidget(self, widg):
        pass


class Window:
    pass


class Application:

    def __init__(self):
        self.data_getter = DataSource()
        self.data_getter.get("param")
        self.data_getter.get("param2")

        self.main_widget = Window()

        self.series1 = Plot(self.main_widget)
        self.series2 = Plot(self.main_widget)
        self.series3 = Plot(self.main_widget)
        self.series4 = Plot(self.main_widget)

        self.button1 = Button("button1")
        self.button1.connect()

        self.button2 = Button("button2")
        self.button2.connect()

        self.button3 = Button("button3")
        self.button3.connect()
        self.button3.toggle()

        self.button4 = Button("button4")
        self.button4.connect()
        self.button4.toggle()

        self.button5 = Button("button5")
        self.button5.connect()
        self.button5.toggle()

        self.button6 = Button("button6")
        self.button6.connect()

        self.button7 = Button("button7")
        self.button7.connect()

        self.series1.compute_initial_figure()
        self.series2.compute_initial_figure()
        self.series3.compute_initial_figure()
        self.series4.compute_initial_figure()

        layout = Layout()
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        layout.addWidget(self.button5)
        layout.addWidget(self.button6)

    def update_plots(self):
        p1 = self.data_getter.get("param3")
        self.series1.append(p1[0])
        self.series2.append(p1[1])
        self.series3.append(p1[2])
        self.series4.append(p1[3])

        p2 = self.data_getter.get("param4")
        self.series1.append(p2[0])
        self.series2.append(p2[1])
        self.series3.append(p2[2])
        self.series4.append(p2[3])

        p3 = self.data_getter.get("param5")
        self.series1.append(p3[0])
        self.series2.append(p3[1])
        self.series3.append(p3[2])
        self.series4.append(p3[3])

        self.series1.update_figure()
        self.series2.update_figure()
        self.series3.update_figure()
        self.series4.update_figure()

    def reset_plots(self):
        p1 = self.data_getter.get("param")
        self.series1.append(p1[0])
        self.series2.append(p1[1])
        self.series3.append(p1[2])
        self.series4.append(p1[3])

        self.series1.reset_figure()
        self.series2.reset_figure()
        self.series3.reset_figure()
        self.series4.reset_figure()

        p2 = self.data_getter.get("param")
