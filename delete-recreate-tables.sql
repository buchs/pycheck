use bookmarks;
drop table urls;
drop table entries;
create table urls (i SERIAL, url VARCHAR(2048));
create table entries (i SERIAL, location VARCHAR(2048), name VARCHAR(2048), file VARCHAR(2048), url BIGINT(20) );
