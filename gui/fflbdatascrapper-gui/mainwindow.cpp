#include <qprocess.h>
#include <qdir.h>

#include "mainwindow.h"
#include "./ui_mainwindow.h"

#include "fflbdatamodel.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    myProcess = new QProcess(this);
    myModel = new FFLBDataModel(myProcess);
}

MainWindow::~MainWindow()
{
    delete ui;
    delete myProcess;
    delete myModel;
}


void MainWindow::on_pushButton_clicked()
{
    QString program = "cd ..;cd .. ;python main.py";


    qInfo() << "Starting a process"; // more info about subprocess.
    myProcess->setProcessChannelMode(QProcess::MergedChannels);
    connect(myProcess, &QProcess::readyReadStandardOutput, this, &MainWindow::readyToRead);
    myProcess->start("powershell.exe", QStringList() << program);

    connect(myProcess, SIGNAL(finished(int)), this, SLOT(readCSV()));
    ui->fflbDataView->setModel(myModel);
}

void MainWindow::readyToRead()
{
    QString output(myProcess->readAllStandardOutput());
    ui->console->append(output);
    //Do something with the string
}

void MainWindow::readCSVData()
{
}

