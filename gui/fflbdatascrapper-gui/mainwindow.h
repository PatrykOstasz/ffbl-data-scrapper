#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class QProcess;
class FFLBDataModel;

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void on_pushButton_clicked();
    void readyToRead();
    void readCSVData();
    void populateData() {}

private:
    Ui::MainWindow *ui;
    QProcess* myProcess;
    FFLBDataModel* myModel;
};
#endif // MAINWINDOW_H
