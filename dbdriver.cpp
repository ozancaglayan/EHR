#include "dbdriver.h"

bool DatabaseManager::openDatabase() {
    // Select SQLite backend
    db = QSqlDatabase::addDatabase("QSQLITE");

    // Generate db path
    QString path(QDir::home().path());
    path.append(QDir::separator()).append(".ehrdb.sqlite");
    path = QDir::toNativeSeparators(path);
    db.setDatabaseName(path);

    // Open Database
    return db.open();
}

bool DatabaseManager::createHealthRecordTable()
{
    bool retval = false;

    if (db.isOpen()) {
        QSqlQuery query;
        retval = query.exec("create table records "
                            "(id integer primary key, "
                            "firstname varchar(30), "
                            "lastname varchar(30), "
                            "birthdate datetime, "
                            "sex nchar(1), "
                            "occupation varchar(50), "
                            "tckimlikno varchar(11), "
                            "sgkno varchar(15), "
                            "email varchar(30), "
                            "address text, "
                            "photo blob, "
                            "firstseen datetime, ");
    }

    return retval;
}

int DatabaseManager::insertRecord(QString firstName,
                                  QString lastName,
                                  QString sgkno,
                                  QString email,
                                  QString firstSeen) {
    bool retval = false;

    if (db.isOpen()) {
        QSQlQuery query;
        ret = query.exec("insert into records values(NULL, '%1, '%2', '%3', '%4', %5")
                   .arg(firstname).arg(lastname).arg(sgkno).arg(email).arg(firstSeen)
