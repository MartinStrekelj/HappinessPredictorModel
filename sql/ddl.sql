create table if not exists happiness_schema.happiness
(
	id serial not null
		constraint happiness_pk
			primary key,
	country varchar(100),
	region varchar(100),
	year integer,
	family double precision,
	health double precision,
	freedom double precision,
	government_trust double precision,
	economy double precision,
	happiness_score double precision,
	generosity numeric
);

comment on column happiness_schema.happiness.health is 'life expectancy';

comment on column happiness_schema.happiness.freedom is 'to act at your free will';

comment on column happiness_schema.happiness.government_trust is 'Corruption';

comment on column happiness_schema.happiness.economy is 'GDP per Capita
';

alter table happiness_schema.happiness owner to postgres;

create unique index if not exists happiness_id_uindex
	on happiness_schema.happiness (id);


