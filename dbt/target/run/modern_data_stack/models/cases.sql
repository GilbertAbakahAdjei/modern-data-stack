

  create or replace view `modern-data-stack-343214`.`dbt_gilbert_prefect`.`cases`
  OPTIONS()
  as select * from `demo_test.demo_test` where new_recovered > new_confirmed;

