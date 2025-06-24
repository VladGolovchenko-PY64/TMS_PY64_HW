create database if not exists lesson14;

use lesson14;

show tables;

create table users (
	id int unsigned primary key auto_increment,
	username varchar(64) not null unique,
	password varchar(64) not null,
	email varchar(64) unique null
);


create table seller (
	id int unsigned primary key auto_increment,
	company varchar(64) not null,
	phone varchar(64) not null
);

create table products (
	id int unsigned primary key auto_increment,
	name varchar(255),
	cost int unsigned not null,
	count int unsigned not null,
	seller_id int unsigned not null,
    foreign key (seller_id) references seller (id)
);

create table orders (
	id int unsigned primary key auto_increment,
	user_id int unsigned not null,
	product_id int unsigned not null,
	count int not null,
    foreign key (user_id) references users (id),
    foreign key (product_id) references products (id)
);

insert users(username, password, email) values ('vlad', '12345678', 'v@v.com');

insert seller(company, phone) values('ibm', '+375 99 1234567');

insert products(name, cost, count, seller_id) values ('phone', 123, 20, 1);

insert orders(user_id, product_id, count) values (1, 1, 10);

select * from users;
select * from seller;
select * from products;
select * from orders;

drop table users;
drop table seller;
drop table products;
drop table orders;

desc users;
desc products;


