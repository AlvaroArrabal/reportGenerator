from Domain.reportGenerator import generate_consolidation_report, generate_expansion_report
from tkinter import *
from tkinter import messagebox, filedialog
import time
import traceback
import sys


def save_error(e, siteName, reportType):
    exc_type, exc_value, exc_traceback = sys.exc_info()

    dateLog = time.strftime("%m_%d_%Y")

    nameLog = '.\\Config\\ErrorLogs\\Errors_' + dateLog + '.txt'

    log = open(nameLog, 'a')

    dateError = time.strftime("- %H:%M:%S -")
    error = traceback.format_exc()
    log.write(
        f"<{dateError}>\nIn {siteName} <{reportType}>:\nexc_type: {exc_type}\nexc_value: {exc_value}\n\n#########\n{error}\n#########\n")
    log.write('-' * 60)
    log.write('\n')


def create(reportType, cells, techs, siteName):
    if cells == 0 or techs == 0:
        messagebox.showerror('Error', 'número de celdas o tecnologías vacia')
    else:
        try:
            babysittingPath = filedialog.askopenfilename(title="Seleccione el informe")
            saveIn = filedialog.askdirectory(title="Seleccione una ubicación para guardar el informe")
            print(babysittingPath)
            yesno = messagebox.askyesno('Información', "No cierre el programa hasta que termine.\n¿Desea continuar?")
            if yesno == True:
                if reportType == 'Consolidación':
                    generate_consolidation_report(cells, techs, siteName, saveIn, babysittingPath)
                else:
                    generate_expansion_report(cells, techs, siteName, saveIn, babysittingPath)
                messagebox.showinfo('Información', 'Terminado!')
            else:
                messagebox.showinfo('Información', 'Operacion cancelada.')
        except Exception as e:
            messagebox.showerror('Error', f'Algo ha ido mal\nError: {e}')
            save_error(e, siteName, reportType)


def display_parameters():
    app = Tk()
    app.geometry("280x138+0+0")
    app.resizable(0, 0)
    app.title("Babysitting C44")
    app.config(bg="white")

    return app


def display_config(app):
    panel = Frame(app, bd=2, relief=FLAT)
    panel.pack(side=TOP)

    Label(panel, text="Nombre Nodo", fg="black", font=("Arial", 10, "bold"), width=11, underline=0).grid(row=0,
                                                                                                         column=1,
                                                                                                         columnspan=2)

    siteName = StringVar()
    reportType = StringVar()
    cells = IntVar()
    techs = IntVar()

    siteName.set("")
    siteNameBox = Entry(panel, font=("Arial", 12), bd=2, width=14, state=NORMAL, textvariable=siteName)
    siteNameBox.grid(row=1, column=1, columnspan=2)

    Label(panel, text="Informe", fg="black", font=("Arial", 10, "bold"), width=15, underline=0).grid(row=2, column=0)
    Label(panel, text="NºSectores", fg="black", font=("Arial", 10, "bold"), width=8, underline=0).grid(row=2, column=1)
    Label(panel, text="NºBandas", fg="black", font=("Arial", 10, "bold"), width=8, underline=0).grid(row=2, column=2)

    options = ['Consolidación', 'Ampliación']

    reportType.set("Consolidación")
    OptionMenu(panel, reportType, *options).grid(row=3, column=0)

    cells.set(0)
    Entry(panel, font=("Arial", 12), bd=1, width=7, state=NORMAL, textvariable=cells).grid(row=3, column=1)

    techs.set(0)
    Entry(panel, font=("Arial", 12), bd=1, width=7, state=NORMAL, textvariable=techs).grid(row=3, column=2)

    button = Button(panel, text='Crear', font=("Arial", 13, "bold"), fg="black", bg="Gray", bd=2, width=6,
                    command=lambda: create(reportType.get(), cells.get(), techs.get(), siteName.get().upper()))
    button.grid(row=4, column=1)

    app.mainloop()
