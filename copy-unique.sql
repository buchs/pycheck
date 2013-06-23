create table unique_entries (location VARCHAR(2048), name VARCHAR(2048), url BIGINT(20) );
insert into unique_entries select distinct location,name,url from entries;
