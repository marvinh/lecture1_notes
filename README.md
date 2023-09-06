# lecture1_notes

# basic legacy app demonstrating HTML forms remember to validate your input 

# if you want to try docker remember to install docker and at the root of your directory call 
# docker-compose build
# docker-compose up

# next step is to build an api 
# so we can serve this to a react SPA

# SQL DUMP

CREATE DATABASE `task_app` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

CREATE TABLE `task` (
  `id` int NOT NULL AUTO_INCREMENT,
  `task_name` varchar(255) NOT NULL,
  `task_description` mediumtext NOT NULL,
  `due_date` datetime DEFAULT NULL,
  `completed_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

#make sure to edit your mysql connection string if you are using an alternate port and password

cd into task_app

>pip3 install -r requiements.txt
>python3 app.py
