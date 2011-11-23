#include <QObject>
#include <QSqlDatabase>
#include <QSqlError>
#include <QSqlQuery>
#include <QString>

class DatabaseManager:public QObject
{
    public:
        DatabaseManager(QObject *parent = 0);
        ~DatabaseManager();

    public:
        bool openDatabase();
        bool createHealthRecord();
        bool searchRecord(QString firstName, QString lastName);
        int  insertRecord(QString firstName, QString lastName,
                          QString sgkno, QString email,
                          QString firstSeen);

    private:
        QSqlDatabase db;
}
