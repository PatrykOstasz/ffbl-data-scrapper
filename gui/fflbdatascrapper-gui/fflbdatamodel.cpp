#include "fflbdatamodel.h"

#include <QProcess>
#include <QFile>

FFLBDataModel::FFLBDataModel(QProcess* process, QObject *parent)
    : QAbstractTableModel(parent)
{
    QObject::connect(process, SIGNAL(finished(int)), this, SLOT(readCSVData()));
}

int FFLBDataModel::rowCount(const QModelIndex & /*parent*/) const
{
    return 2;
}

int FFLBDataModel::columnCount(const QModelIndex & /*parent*/) const
{
    return 3;
}

QVariant FFLBDataModel::data(const QModelIndex &index, int role) const
{
//    if (role == Qt::DisplayRole)
//        return QString("Row%1, Column%2")
//            .arg(index.row() + 1)
//            .arg(index.column() +1);

    return QVariant();
}

void FFLBDataModel::readCSVData()
{
    //ui->console->append(QString("Hello There"));

    QFile file("../../example.csv");
    if (file.open(QIODevice::ReadOnly)) {

        int lineindex = 0;                     // file line counter
        QTextStream in(&file);                 // read to text stream

        while (!in.atEnd()) {

            // read one line from textstream(separated by "\n")
            QString fileLine = in.readLine();

            // parse the read line into separate pieces(tokens) with "," as the delimiter
            QStringList lineToken = fileLine.split(";");

            // load parsed data to model accordingly
            for (int j = 0; j < lineToken.size(); j++) {
                qDebug() << lineToken.at(j);
                //QStandardItem *item = new QStandardItem(value);
                //model->setItem(lineindex, j, item);
            }

            lineindex++;
        }

        file.close();
    }
}
