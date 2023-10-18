#include "fflbdatamodel.h"

FFLBDataModel::FFLBDataModel(QObject *parent)
    : QAbstractTableModel(parent)
{
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
    if (role == Qt::DisplayRole)
        return QString("Row%1, Column%2")
            .arg(index.row() + 1)
            .arg(index.column() +1);

    return QVariant();
}
