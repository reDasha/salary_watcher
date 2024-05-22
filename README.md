## Salary Watcher
REST-сервис, который по запросу сотрудника предоставляет информацию о его текущей зарплате и дате следующего повышения.

Сервис также позволяет зарегистрировать нового пользователя. Его имя email и пароль (в хэшированном виде) хранятся в базе данных Postgres. Информация о зарплате и дате повышения сотрудника заполняется отдельно. 

### Чтобы установить сервис:
- ...

### Чтобы воспользоваться сервисом сотрудник должен:
- залогиниться на странице, введя логин (email) и пароль;
- в течение одного часа (срок действия токена) зайти на страницу /salary и нажать на кнопку "execute".

