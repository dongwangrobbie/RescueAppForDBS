-- This file contains the definitions of the tables used in the application.
--
-- Part table
-- create table parts(pid serial primary key, pname varchar(20), pmaterial varchar(10), pcolor varchar(10), pprice float);
--
-- -- Supplier table
-- create table supplier(sid serial primary key, sname varchar(10), scity varchar(10), sphone varchar(10));
--
-- -- Supplies table
-- create table supplies(pid integer references Parts(pid), sid integer references
-- Supplier(sid), qty integer, primary key(pid, sid));
--
-- -- PartSales table
-- create table partsales(psaleid serial primary key, pid integer references Parts(pid),
-- sid integer references Supplier(sid), sqty integer, sprice float, sdate Date);

CREATE TABLE user(
  user_id serial primary key,
  category varchar(20)
);

CREATE TABLE administrator(
  admin_id serial primary key,
  user_id integer references user(user_id),
  admin_name varchar(20),
  admin_passwd varchar(20)
);

CREATE TABLE consumer(
  consumer_id serial primary key,
  uid integer references puser(id),
  category varchar(10),
  first_name varchar(20),
  last_name varchar(20),
  payment_method  varchar(10),
  address varchar(50),
  phone varchar(10)
);

CREATE TABLE supplier(
  supplier_id serial primary key,
  user_id integer references user(user_id),
  phone varchar(10)
);

CREATE TABLE company(
  company_id serial primary key,
  com_name varchar(20),
  com_city varchar(20)
);

CREATE TABLE resource(
  resource_id serial primary key,
  res_type <type>,
  res_price <type>,
);

CREATE TABLE reservation(
  reservation_id serial primary key,
  res_name varchar(20),
  res_avalability <type>,
  res_address <type>
);

CREATE TABLE order(
  order_id serial primary key,
  resource_id integer references resource(resource_id),
  res_name varchar(20),
  res_need varchar(20),
  res_price varchar(20)
);

CREATE TABLE paymethod(
  payment_id serial primary key,
  category varchar(20),
);

