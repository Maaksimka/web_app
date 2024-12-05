from database import db


# Вставка данных в коллекцию 'Buyers'
db.Buyers.insert_many([
    { "buyer_id": 1, "fio": "Троцкий Владислав Владимирович", "phone_number": "+79110001122", "email": "trotsky@example.com" },
    { "buyer_id": 2, "fio": "Аболтин Моисей Викторович", "phone_number": "+79120002233", "email": "aboltin@example.com" },
    { "buyer_id": 3, "fio": "Бегун Карина Сергеевна", "phone_number": "+79130003344", "email": "begunk@example.com" },
    { "buyer_id": 4, "fio": "Анискевич Денис Алексеевич", "phone_number": "+79140004455", "email": "anisk@example.com" },
    { "buyer_id": 5, "fio": "Гузаревич Кирилл Сергеевич", "phone_number": "+79150005566", "email": "guzarv@example.com" },
    { "buyer_id": 6, "fio": "Воробей Антон Александрович", "phone_number": "+79160006677", "email": "vorobey@example.com" },
    { "buyer_id": 7, "fio": "Кудош Дарья Васильевна", "phone_number": "+79170007788", "email": "kudosh@example.com" },
    { "buyer_id": 8, "fio": "Загорец Александра Андреевна", "phone_number": "+79180008899", "email": "zagorec@example.com" },
    { "buyer_id": 9, "fio": "Климук Павел Владимирович", "phone_number": "+79190009911", "email": "klimuk@example.com" },
    { "buyer_id": 10, "fio": "Зайцев Никита Сергеевич", "phone_number": "+79200001122", "email": "zaycev@example.com" }
])

# Вставка данных в коллекцию 'Customers'
db.Customers.insert_many([
    { "customer_id": 1, "fio": "Кудрицкая Валерия Викторовна", "email": "kudrickaya@example.com", "phone_number": "+79210002233", "date_of_birth": "1990-01-01", "registration_date": "2023-01-15" },
    { "customer_id": 2, "fio": "Матюкевич Александра Александровна", "email": "matyukevich@example.com", "phone_number": "+79220003344", "date_of_birth": "1985-02-02", "registration_date": "2023-02-20" },
    { "customer_id": 3, "fio": "Мишпилькина Ангелина Викторовна", "email": "mishp@example.com", "phone_number": "+79230004455", "date_of_birth": "1992-03-03", "registration_date": "2023-03-10" },
    { "customer_id": 4, "fio": "Панасеня Максим Александрович", "email": "panasenya@example.com", "phone_number": "+79240005566", "date_of_birth": "1980-04-04", "registration_date": "2023-04-05" },
    { "customer_id": 5, "fio": "Чепелевич Арсений Петрович", "email": "chepelevich@example.com", "phone_number": "+79250006677", "date_of_birth": "1995-05-05", "registration_date": "2023-05-12" },
    { "customer_id": 6, "fio": "Посканной Иван Андреевич", "email": "poskannoi@example.com", "phone_number": "+79260007788", "date_of_birth": "1998-06-06", "registration_date": "2023-06-25" },
    { "customer_id": 7, "fio": "Малявский Александр Викторович", "email": "malyavsky@example.com", "phone_number": "+79270008899", "date_of_birth": "1991-07-07", "registration_date": "2023-07-01" },
    { "customer_id": 8, "fio": "Ласков Артем Денисович", "email": "laskov@example.com", "phone_number": "+79280009911", "date_of_birth": "1987-08-08", "registration_date": "2023-08-19" },
    { "customer_id": 9, "fio": "Лысковец Никита Александрович", "email": "lyskovets@example.com", "phone_number": "+79290001122", "date_of_birth": "1993-09-09", "registration_date": "2023-09-05" },
    { "customer_id": 10, "fio": "Терехова Алина Викторовна", "email": "terekhova@example.com", "phone_number": "+79300002233", "date_of_birth": "1990-10-10", "registration_date": "2023-10-02" }
])

# Вставка данных в коллекцию 'Dealers'
db.Dealers.insert_many([
    { "dealer_id": 1, "fio": "Иосиф Висарионович Сталин", "phone_number": "+79410001122", "email": "stalin@example.com", "working_hours": "09:00-18:00" },
    { "dealer_id": 2, "fio": "Владимир Владимирович Путин", "phone_number": "+79420002233", "email": "putin@example.com", "working_hours": "08:00-17:00" },
    { "dealer_id": 3, "fio": "Ким Чен Ын", "phone_number": "+79430003344", "email": "kim@example.com", "working_hours": "10:00-19:00" },
    { "dealer_id": 4, "fio": "Дональд Александрович Трамп", "phone_number": "+79440004455", "email": "trump@example.com", "working_hours": "07:00-16:00" },
    { "dealer_id": 5, "fio": "Владимир Ильич Ленин", "phone_number": "+79450005566", "email": "lenin@example.com", "working_hours": "09:30-18:30" }
])

db.Cars.insert_many([
    {
        "car_id": 1,
        "brand": "Toyota",
        "model": "Camry",
        "year": 2021,
        "mileage": 150009,
        "price": 2500000,
        "commissions": 125000, # 5% от 2500000
        "photo": "https://tinyurl.com/yo7b62bo"
    },
    {
        "car_id": 21,
        "brand": "Honda",
        "model": "Accord",
        "year": 2011,
        "mileage": 277425,
        "price": 3438548,
        "commissions": 171927, # 5% от 3438548
        "photo": "https://tinyurl.com/ytdcrhd6"
    },
    {
        "car_id": 2,
        "brand": "Honda",
        "model": "Civic",
        "year": 2016,
        "mileage": 181473,
        "price": 2592598,
        "commissions": 129629, # 5% от 2592598
        "photo": "https://tinyurl.com/yw348kwz"
    },
    {
        "car_id": 3,
        "brand": "Honda",
        "model": "CR-V",
        "year": 2005,
        "mileage": 109894,
        "price": 1749705,
        "commissions": 87485, # 5% от 1749705
        "photo": "https://tinyurl.com/ysx2vl8r"
    },
    {
        "car_id": 4,
        "brand": "Mercedes",
        "model": "C-Class",
        "year": 2008,
        "mileage": 229428,
        "price": 2852309,
        "commissions": 142615, # 5% от 2852309
        "photo": "https://tinyurl.com/yp2kt7ao"
    },
    {
        "car_id": 5,
        "brand": "Kia",
        "model": "Sorento",
        "year": 2010,
        "mileage": 156060,
        "price": 1296085,
        "commissions": 64804, # 5% от 1296085
        "photo": "https://tinyurl.com/ytxtqgf2"
    },
    {
        "car_id": 6,
        "brand": "Toyota",
        "model": "Camry",
        "year": 2013,
        "mileage": 47364,
        "price": 2244017,
        "commissions": 112200, # 5% от 2244017
        "photo": "https://tinyurl.com/ywtehjsa"
    },
    {
        "car_id": 7,
        "brand": "Hyundai",
        "model": "Elantra",
        "year": 2017,
        "mileage": 206980,
        "price": 3746712,
        "commissions": 187335, # 5% от 3746712
        "photo": "https://tinyurl.com/yn3krw57"
    },
    {
        "car_id": 8,
        "brand": "Kia",
        "model": "Sorento",
        "year": 2018,
        "mileage": 106911,
        "price": 2674990,
        "commissions": 133749, # 5% от 2674990
        "photo": "https://tinyurl.com/ytq6fmtm"
    },
    {
        "car_id": 9,
        "brand": "Kia",
        "model": "Sportage",
        "year": 2014,
        "mileage": 201903,
        "price": 2229132,
        "commissions": 111456, # 5% от 2229132
        "photo": "https://tinyurl.com/yunrwh9b"
    },
    {
        "car_id": 10,
        "brand": "Toyota",
        "model": "Camry",
        "year": 2019,
        "mileage": 55122,
        "price": 3973789,
        "commissions": 198689, # 5% от 3973789
        "photo": "https://tinyurl.com/yqzess4v"
    },
    {
        "car_id": 11,
        "brand": "Chevrolet",
        "model": "Camaro",
        "year": 2019,
        "mileage": 145036,
        "price": 3491333,
        "commissions": 174566, # 5% от 3491333
        "photo": "https://tinyurl.com/yw3nnzb7"
    },
    {
        "car_id": 12,
        "brand": "Honda",
        "model": "Civic",
        "year": 2005,
        "mileage": 162117,
        "price": 534668,
        "commissions": 26733, # 5% от 534668
        "photo": "https://tinyurl.com/2xc9w2l8"
    },
    {
        "car_id": 13,
        "brand": "Kia",
        "model": "Optima",
        "year": 2012,
        "mileage": 55217,
        "price": 4312310,
        "commissions": 215615, # 5% от 4312310
        "photo": "https://tinyurl.com/ymvyuu5u"
    },
    {
        "car_id": 14,
        "brand": "BMW",
        "model": "3 Series",
        "year": 2010,
        "mileage": 107360,
        "price": 3451602,
        "commissions": 172580, # 5% от 3451602
        "photo": "https://tinyurl.com/yroy3duj"
    },
    {
        "car_id": 15,
        "brand": "Kia",
        "model": "Sportage",
        "year": 2008,
        "mileage": 22397,
        "price": 812539,
        "commissions": 40626, # 5% от 812539
        "photo": "https://tinyurl.com/yktvupdy"
    },
    {
        "car_id": 16,
        "brand": "Mercedes",
        "model": "GLA",
        "year": 2011,
        "mileage": 239970,
        "price": 1226713,
        "commissions": 61335, # 5% от 1226713
        "photo": "https://tinyurl.com/ynwwu8ae"
    },
    {
        "car_id": 17,
        "brand": "BMW",
        "model": "X5",
        "year": 2021,
        "mileage": 7040,
        "price": 3478060,
        "commissions": 173903, # 5% от 3478060
        "photo": "https://tinyurl.com/ynyu8zs9"
    },
    {
        "car_id": 18,
        "brand": "Honda",
        "model": "CR-V",
        "year": 2006,
        "mileage": 195320,
        "price": 900218,
        "commissions": 45010, # 5% от 900218
        "photo": "https://tinyurl.com/ylokdl8a"
    },
    {
        "car_id": 19,
        "brand": "Honda",
        "model": "Accord",
        "year": 2008,
        "mileage": 75751,
        "price": 2695630,
        "commissions": 134781, # 5% от 2695630
        "photo": "https://tinyurl.com/yp6pylqd"
    }
]);



db.Contracts.insert_many([
  { "contract_id": 1, "car_id": 1, "customer_id": 1, "dealer_id": 1, "dealer_fio": "Иосиф Висарионович Сталин", "customer_fio": "Кудрицкая Валерия Викторовна", "car_brand": "Toyota", "car_model": "Camry", "car_year": 2021, "price": 2625000, "contract_date": "2024-11-25" },
  { "contract_id": 2, "car_id": 21, "customer_id": 2, "dealer_id": 2, "dealer_fio": "Владимир Владимирович Путин", "customer_fio": "Матюкевич Александра Александровна", "car_brand": "Honda", "car_model": "Accord", "car_year": 2011, "price": 3600475, "contract_date": "2024-11-26" },
  { "contract_id": 3, "car_id": 2, "customer_id": 3, "dealer_id": 3, "dealer_fio": "Ким Чен Ын", "customer_fio": "Мишпилькина Ангелина Викторовна", "car_brand": "Honda", "car_model": "Civic", "car_year": 2016, "price": 2722227, "contract_date": "2024-11-27" },
  { "contract_id": 4, "car_id": 3, "customer_id": 4, "dealer_id": 4, "dealer_fio": "Дональд Александрович Трамп", "customer_fio": "Панасеня Максим Александрович", "car_brand": "Honda", "car_model": "CR-V", "car_year": 2005, "price": 1835190, "contract_date": "2024-11-28" },
  { "contract_id": 5, "car_id": 4, "customer_id": 5, "dealer_id": 5, "dealer_fio": "Владимир Ильич Ленин", "customer_fio": "Чепелевич Арсений Петрович", "car_brand": "Mercedes", "car_model": "C-Class", "car_year": 2008, "price": 2994924, "contract_date": "2024-11-29" },
  { "contract_id": 6, "car_id": 5, "customer_id": 6, "dealer_id": 1, "dealer_fio": "Иосиф Висарионович Сталин", "customer_fio": "Посканной Иван Андреевич", "car_brand": "Kia", "car_model": "Sorento", "car_year": 2010, "price": 1361889, "contract_date": "2024-11-30" },
  { "contract_id": 7, "car_id": 6, "customer_id": 7, "dealer_id": 2, "dealer_fio": "Владимир Владимирович Путин", "customer_fio": "Кудош Дарья Васильевна", "car_brand": "Toyota", "car_model": "Camry", "car_year": 2013, "price": 2356217, "contract_date": "2024-12-01" },
  { "contract_id": 8, "car_id": 7, "customer_id": 8, "dealer_id": 3, "dealer_fio": "Ким Чен Ын", "customer_fio": "Загорец Александра Андреевна", "car_brand": "Hyundai", "car_model": "Elantra", "car_year": 2017, "price": 3932047, "contract_date": "2024-12-02" },
  { "contract_id": 9, "car_id": 8, "customer_id": 9, "dealer_id": 4, "dealer_fio": "Дональд Александрович Трамп", "customer_fio": "Климук Павел Владимирович", "car_brand": "Kia", "car_model": "Sorento", "car_year": 2018, "price": 2808739, "contract_date": "2024-12-03" },
  { "contract_id": 10, "car_id": 9, "customer_id": 10, "dealer_id": 5, "dealer_fio": "Владимир Ильич Ленин", "customer_fio": "Зайцев Никита Сергеевич", "car_brand": "Kia", "car_model": "Sportage", "car_year": 2014, "price": 2340588, "contract_date": "2024-12-04" },
  { "contract_id": 11, "car_id": 10, "customer_id": 1, "dealer_id": 1, "dealer_fio": "Иосиф Висарионович Сталин", "customer_fio": "Кудрицкая Валерия Викторовна", "car_brand": "Toyota", "car_model": "Camry", "car_year": 2019, "price": 4172478, "contract_date": "2024-12-05" },
  { "contract_id": 12, "car_id": 11, "customer_id": 2, "dealer_id": 2, "dealer_fio": "Владимир Владимирович Путин", "customer_fio": "Матюкевич Александра Александровна", "car_brand": "Chevrolet", "car_model": "Camaro", "car_year": 2019, "price": 3665899, "contract_date": "2024-12-06" },
  { "contract_id": 13, "car_id": 12, "customer_id": 3, "dealer_id": 3, "dealer_fio": "Ким Чен Ын", "customer_fio": "Мишпилькина Ангелина Викторовна", "car_brand": "Honda", "car_model": "Civic", "car_year": 2005, "price": 561901, "contract_date": "2024-12-07" },
  { "contract_id": 14, "car_id": 13, "customer_id": 4, "dealer_id": 4, "dealer_fio": "Дональд Александрович Трамп", "customer_fio": "Панасеня Максим Александрович", "car_brand": "Kia", "car_model": "Optima", "car_year": 2012, "price": 4527925, "contract_date": "2024-12-08" },
  { "contract_id": 15, "car_id": 14, "customer_id": 5, "dealer_id": 5, "dealer_fio": "Владимир Ильич Ленин", "customer_fio": "Чепелевич Арсений Петрович", "car_brand": "BMW", "car_model": "3 Series", "car_year": 2010, "price": 3627182, "contract_date": "2024-12-09" },
  { "contract_id": 16, "car_id": 15, "customer_id": 6, "dealer_id": 1, "dealer_fio": "Иосиф Висарионович Сталин", "customer_fio": "Посканной Иван Андреевич", "car_brand": "Kia", "car_model": "Sportage", "car_year": 2008, "price": 853165, "contract_date": "2024-12-10" },
  { "contract_id": 17, "car_id": 16, "customer_id": 7, "dealer_id": 2, "dealer_fio": "Владимир Владимирович Путин", "customer_fio": "Кудош Дарья Васильевна", "car_brand": "Mercedes", "car_model": "GLA", "car_year": 2011, "price": 1283048, "contract_date": "2024-12-11" },
  { "contract_id": 18, "car_id": 17, "customer_id": 8, "dealer_id": 3, "dealer_fio": "Ким Чен Ын", "customer_fio": "Загорец Александра Андреевна", "car_brand": "BMW", "car_model": "X5", "car_year": 2021, "price": 3656963, "contract_date": "2024-12-12" },
  { "contract_id": 19, "car_id": 18, "customer_id": 9, "dealer_id": 4, "dealer_fio": "Дональд Александрович Трамп", "customer_fio": "Климук Павел Владимирович", "car_brand": "Honda", "car_model": "CR-V", "car_year": 2006, "price": 945228, "contract_date": "2024-12-13" },
  { "contract_id": 20, "car_id": 19, "customer_id": 10, "dealer_id": 5, "dealer_fio": "Владимир Ильич Ленин", "customer_fio": "Зайцев Никита Сергеевич", "car_brand": "Chevrolet", "car_model": "Malibu", "car_year": 2010, "price": 1222785, "contract_date": "2024-12-14" }
]);


db.Pre_sale_actions.insert_many([
  { "action_id": 1, "contract_id": 1, "car_brand": "Toyota", "car_model": "Camry", "car_year": 2021, "inspection_report": "Проверка тормозной системы, замена колодок, замена масла в трансмиссии, чистка салона", "cost": 15000 },
  { "action_id": 2, "contract_id": 2, "car_brand": "Honda", "car_model": "Accord", "car_year": 2011, "inspection_report": "Проверка системы кондиционирования, замена фильтров, полировка кузова, чистка салона", "cost": 13000 },
  { "action_id": 3, "contract_id": 3, "car_brand": "Honda", "car_model": "Civic", "car_year": 2016, "inspection_report": "Проверка подвески, замена амортизаторов, проверка тормозов, чистка салона", "cost": 12000 },
  { "action_id": 4, "contract_id": 4, "car_brand": "Honda", "car_model": "CR-V", "car_year": 2005, "inspection_report": "Проверка двигателя, замена ремня ГРМ, полировка кузова, восстановление тормозных дисков", "cost": 14000 },
  { "action_id": 5, "contract_id": 5, "car_brand": "Mercedes", "car_model": "C-Class", "car_year": 2008, "inspection_report": "Полировка кузова, замена масла, проверка аккумулятора, ремонт системы охлаждения", "cost": 18000 },
  { "action_id": 6, "contract_id": 6, "car_brand": "Kia", "car_model": "Sorento", "car_year": 2010, "inspection_report": "Проверка трансмиссии, замена тормозных колодок, чистка салона, восстановление кузова", "cost": 16000 },
  { "action_id": 7, "contract_id": 7, "car_brand": "Toyota", "car_model": "Camry", "car_year": 2013, "inspection_report": "Проверка системы кондиционирования, замена фильтров, полировка кузова, чистка салона", "cost": 15000 },
  { "action_id": 8, "contract_id": 8, "car_brand": "Hyundai", "car_model": "Elantra", "car_year": 2017, "inspection_report": "Проверка подвески, замена амортизаторов, восстановление тормозных дисков, ремонт кузова", "cost": 17000 },
  { "action_id": 9, "contract_id": 9, "car_brand": "Kia", "car_model": "Sorento", "car_year": 2018, "inspection_report": "Проверка двигателя, замена ремня ГРМ, полировка кузова, чистка салона", "cost": 14000 },
  { "action_id": 10, "contract_id": 10, "car_brand": "Kia", "car_model": "Sportage", "car_year": 2014, "inspection_report": "Проверка системы охлаждения, замена масла, ремонт тормозной системы, полировка кузова", "cost": 12000 },
  { "action_id": 11, "contract_id": 11, "car_brand": "Toyota", "car_model": "Camry", "car_year": 2019, "inspection_report": "Проверка подвески, замена амортизаторов, чистка салона, замена тормозных дисков", "cost": 13000 },
  { "action_id": 12, "contract_id": 12, "car_brand": "Chevrolet", "car_model": "Camaro", "car_year": 2019, "inspection_report": "Проверка трансмиссии, замена фильтров, восстановление кузова, полировка фар", "cost": 14000 },
  { "action_id": 13, "contract_id": 13, "car_brand": "Honda", "car_model": "Civic", "car_year": 2005, "inspection_report": "Проверка тормозной системы, замена колодок, восстановление кузова, замена фильтров", "cost": 11000 },
  { "action_id": 14, "contract_id": 14, "car_brand": "Kia", "car_model": "Optima", "car_year": 2012, "inspection_report": "Проверка аккумулятора, замена масла, полировка кузова, чистка салона", "cost": 13000 },
  { "action_id": 15, "contract_id": 15, "car_brand": "BMW", "car_model": "3 Series", "car_year": 2010, "inspection_report": "Проверка системы кондиционирования, замена фильтров, восстановление кузова, проверка подвески", "cost": 20000 },
  { "action_id": 16, "contract_id": 16, "car_brand": "Kia", "car_model": "Sportage", "car_year": 2008, "inspection_report": "Проверка тормозной системы, замена колодок, полировка кузова, чистка салона", "cost": 10000 },
  { "action_id": 17, "contract_id": 17, "car_brand": "Mercedes", "car_model": "GLA", "car_year": 2011, "inspection_report": "Проверка подвески, замена амортизаторов, восстановление тормозных дисков, полировка кузова", "cost": 15000 },
  { "action_id": 18, "contract_id": 18, "car_brand": "BMW", "car_model": "X5", "car_year": 2021, "inspection_report": "Проверка трансмиссии, замена фильтров, полировка кузова, восстановление кузова", "cost": 16000 },
  { "action_id": 19, "contract_id": 19, "car_brand": "Honda", "car_model": "CR-V", "car_year": 2006, "inspection_report": "Проверка тормозной системы, замена колодок, ремонт кузова, чистка салона", "cost": 12000 },
  { "action_id": 20, "contract_id": 20, "car_brand": "Chevrolet", "car_model": "Malibu", "car_year": 2010, "inspection_report": "Проверка подвески, замена амортизаторов, полировка кузова, восстановление тормозных дисков", "cost": 14000 }
]);



db.Final_contract.insert_many([
  {
    "f_contract_id": 1,
    "buyer_id": 1,
    "contract_id": 1,
    "action_id": 1,
    "customer_fio": "Кудрицкая Валерия Викторовна",
    "buyer_fio": "Троцкий Владислав Владимирович",
    "trusted_person": "Нет",
    "car_brand": "Toyota",
    "car_model": "Camry",
    "car_year": "2021",
    "final_price": "2,515,000",
    "contract_date": "2024-11-27"
  },
  {
    "f_contract_id": 2,
    "buyer_id": 2,
    "contract_id": 2,
    "action_id": 2,
    "customer_fio": "Матюкевич Александра Александровна",
    "buyer_fio": "Аболтин Моисей Викторович",
    "trusted_person": "Нет",
    "car_brand": "Honda",
    "car_model": "Accord",
    "car_year": "2011",
    "final_price": "3,485,548",
    "contract_date": "2024-11-27"
  },
  {
    "f_contract_id": 3,
    "buyer_id": 3,
    "contract_id": 3,
    "action_id": 3,
    "customer_fio": "Мишпилькина Ангелина Викторовна",
    "buyer_fio": "Бегун Карина Сергеевна",
    "trusted_person": "Нет",
    "car_brand": "Honda",
    "car_model": "Civic",
    "car_year": "2016",
    "final_price": "2,692,598",
    "contract_date": "2024-11-27"
  },
  {
    "f_contract_id": 4,
    "buyer_id": 4,
    "contract_id": 4,
    "action_id": 4,
    "customer_fio": "Панасеня Максим Александрович",
    "buyer_fio": "Анискевич Денис Алексеевич",
    "trusted_person": "Нет",
    "car_brand": "Honda",
    "car_model": "CR-V",
    "car_year": "2005",
    "final_price": "1,759,705",
    "contract_date": "2024-11-27"
  },
  {
    "f_contract_id": 5,
    "buyer_id": 5,
    "contract_id": 5,
    "action_id": 5,
    "customer_fio": "Чепелевич Арсений Петрович",
    "buyer_fio": "Гузаревич Кирилл Сергеевич",
    "trusted_person": "Нет",
    "car_brand": "Mercedes",
    "car_model": "C-Class",
    "car_year": "2008",
    "final_price": "2,862,309",
    "contract_date": "2024-11-27"
  },
  {
    "f_contract_id": 6,
    "buyer_id": 6,
    "contract_id": 6,
    "action_id": 6,
    "customer_fio": "Посканной Иван Андреевич",
    "buyer_fio": "Воробей Антон Александрович",
    "trusted_person": "Нет",
    "car_brand": "Kia",
    "car_model": "Sorento",
    "car_year": "2010",
    "final_price": "1,310,085",
    "contract_date": "2024-11-27"
  },
  {
    "f_contract_id": 7,
    "buyer_id": 7,
    "contract_id": 7,
    "action_id": 7,
    "customer_fio": "Малявский Александр Викторович",
    "buyer_fio": "Кудош Дарья Васильевна",
    "trusted_person": "Нет",
    "car_brand": "Toyota",
    "car_model": "Camry",
    "car_year": "2013",
    "final_price": "2,360,017",
    "contract_date": "2024-11-27"
  },
  {
    "f_contract_id": 8,
    "buyer_id": 8,
    "contract_id": 8,
    "action_id": 8,
    "customer_fio": "Ласков Артем Денисович",
    "buyer_fio": "Загорец Александра Андреевна",
    "trusted_person": "Нет",
    "car_brand": "Hyundai",
    "car_model": "Elantra",
    "car_year": "2017",
    "final_price": "3,746,712",
    "contract_date": "2024-11-27"
  },
  {
    "f_contract_id": 9,
    "buyer_id": 9,
    "contract_id": 9,
    "action_id": 9,
    "customer_fio": "Лысковец Никита Александрович",
    "buyer_fio": "Климук Павел Владимирович",
    "trusted_person": "Нет",
    "car_brand": "Kia",
    "car_model": "Sorento",
    "car_year": "2018",
    "final_price": "2,804,990",
    "contract_date": "2024-11-27"
  },
  {
    "f_contract_id": 10,
    "buyer_id": 10,
    "contract_id": 10,
    "action_id": 10,
    "customer_fio": "Терехова Алина Викторовна",
    "buyer_fio": "Зайцев Никита Сергеевич",
    "trusted_person": "Нет",
    "car_brand": "Kia",
    "car_model": "Sportage",
    "car_year": "2014",
    "final_price": "2,329,132",
    "contract_date": "2024-11-27"
  },
  {
    "f_contract_id": 11,
    "buyer_id": 1,
    "contract_id": 11,
    "action_id": 11,
    "customer_fio": "Кудрицкая Валерия Викторовна",
    "buyer_fio": "Троцкий Владислав Владимирович",
    "trusted_person": "Нет",
    "car_brand": "Toyota",
    "car_model": "Camry",
    "car_year": "2019",
    "final_price": "4,007,478",
    "contract_date": "2024-11-27"
  },
  {
    "f_contract_id": 12,
    "buyer_id": 2,
    "contract_id": 12,
    "action_id": 12,
    "customer_fio": "Матюкевич Александра Александровна",
    "buyer_fio": "Аболтин Моисей Викторович",
    "trusted_person": "Нет",
    "car_brand": "Chevrolet",
    "car_model": "Camaro",
    "car_year": "2019",
    "final_price": "3,614,133",
    "contract_date": "2024-11-27"
  },
  {
    "f_contract_id": 13,
    "buyer_id": 3,
    "contract_id": 13,
    "action_id": 13,
    "customer_fio": "Мишпилькина Ангелина Викторовна",
    "buyer_fio": "Бегун Карина Сергеевна",
    "trusted_person": "Нет",
    "car_brand": "Honda",
    "car_model": "Civic",
    "car_year": "2005",
    "final_price": "591,901",
    "contract_date": "2024-11-27"
  },
  {
    "f_contract_id": 14,
    "buyer_id": 4,
    "contract_id": 14,
    "action_id": 14,
    "customer_fio": "Панасеня Максим Александрович",
    "buyer_fio": "Анискевич Денис Алексеевич",
    "trusted_person": "Нет",
    "car_brand": "Kia",
    "car_model": "Optima",
    "car_year": "2012",
    "final_price": "4,312,310",
    "contract_date": "2024-11-27"
  },
  {
    "f_contract_id": 15,
    "buyer_id": 5,
    "contract_id": 15,
    "action_id": 15,
    "customer_fio": "Чепелевич Арсений Петрович",
    "buyer_fio": "Гузаревич Кирилл Сергеевич",
    "trusted_person": "Нет",
    "car_brand": "Mercedes",
    "car_model": "C-Class",
    "car_year": "2012",
    "final_price": "3,156,000",
    "contract_date": "2024-11-27"
  },
  {
    "f_contract_id": 16,
    "buyer_id": 6,
    "contract_id": 16,
    "action_id": 16,
    "customer_fio": "Посканной Иван Андреевич",
    "buyer_fio": "Воробей Антон Александрович",
    "trusted_person": "Нет",
    "car_brand": "Hyundai",
    "car_model": "Tucson",
    "car_year": "2015",
    "final_price": "2,230,500",
    "contract_date": "2024-11-27"
  },
  {
    "f_contract_id": 17,
    "buyer_id": 7,
    "contract_id": 17,
    "action_id": 17,
    "customer_fio": "Малявский Александр Викторович",
    "buyer_fio": "Кудош Дарья Васильевна",
    "trusted_person": "Нет",
    "car_brand": "Nissan",
    "car_model": "X-Trail",
    "car_year": "2020",
    "final_price": "3,578,000",
    "contract_date": "2024-11-27"
  },
  {
    "f_contract_id": 18,
    "buyer_id": 8,
    "contract_id": 18,
    "action_id": 18,
    "customer_fio": "Ласков Артем Денисович",
    "buyer_fio": "Загорец Александра Андреевна",
    "trusted_person": "Нет",
    "car_brand": "BMW",
    "car_model": "X5",
    "car_year": "2017",
    "final_price": "4,012,150",
    "contract_date": "2024-11-27"
  },
  {
    "f_contract_id": 19,
    "buyer_id": 9,
    "contract_id": 19,
    "action_id": 19,
    "customer_fio": "Лысковец Никита Александрович",
    "buyer_fio": "Климук Павел Владимирович",
    "trusted_person": "Нет",
    "car_brand": "Mazda",
    "car_model": "CX-5",
    "car_year": "2016",
    "final_price": "2,620,000",
    "contract_date": "2024-11-27"
  },
  {
    "f_contract_id": 20,
    "buyer_id": 10,
    "contract_id": 20,
    "action_id": 20,
    "customer_fio": "Терехова Алина Викторовна",
    "buyer_fio": "Зайцев Никита Сергеевич",
    "trusted_person": "Нет",
    "car_brand": "Ford",
    "car_model": "Focus",
    "car_year": "2015",
    "final_price": "1,980,000",
    "contract_date": "2024-11-27"
  }
]);
