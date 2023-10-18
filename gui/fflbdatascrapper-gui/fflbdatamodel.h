#ifndef FFLBDATAMODEL_H
#define FFLBDATAMODEL_H

#include <QAbstractTableModel>

class FFLBDataModel : public QAbstractTableModel
{
    Q_OBJECT

public:
    explicit FFLBDataModel(QObject *parent = nullptr);

    int rowCount(const QModelIndex &parent = QModelIndex()) const override;
    int columnCount(const QModelIndex &parent = QModelIndex()) const override;
    QVariant data(const QModelIndex &index, int role = Qt::DisplayRole) const override;
};

#endif // FFLBDATAMODEL_H
