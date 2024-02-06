# Nebula

These instructions will help students to clone and host the React app on their GitHub Pages.

### Prerequisites

- GitHub account

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/lawrencemuema/Nebula.git
   cd Nebula

   git checkout -b gh-pages

   git add .
   git commit -m "Add build files for GitHub Pages"
   git push origin gh-pages
   ```

2. **Using Github webpage:**

   ```bash
   Go to your GitHub repository.
   Navigate to "Settings" > "Pages" in the sidebar.
   Select the "gh-pages" branch and the "root" directory.
   ```


After a few minutes, your React app will be available at https://your-username.github.io/your-repo/.

*If you face any redirection issues please reload the homepage: [yourgh-pages/Nebula](https://your-username.github.io/your-repo/.)https://your-username.github.io/your-repo/.


**Project steps**


# Basic CRUD: Flask & PostgreSQL

1. Activate __PostgreSQL__ server:
    
    ```bash
    $ cd C:\Program Files\PostgreSQL\16\bin
    $ psql -U postgres
      Password for user postgres: <insert password here>
    ```

#

2. Create a database on PostgreSQL, my database name is __"lin_flask"__:
    
    ```bash
    postgres=#  CREATE DATABASE lin_flask;
    postgres=#  \l 
    postgres=#  \c lin_flask
    ``` 

#

3. import these
-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 26, 2024 at 09:26 AM
-- Server version: 8.0.34
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `lin_flask`
--

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `id` int NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `email` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `attendance_average` decimal(5,2) NOT NULL,
  `assignment_completion` int NOT NULL,
  `ranking` int NOT NULL,
  `cohort` varchar(255) COLLATE utf8mb4_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`id`, `name`, `email`, `attendance_average`, `assignment_completion`, `ranking`, `cohort`) VALUES
(1, 'John Doe', 'johndoe@example.com', 90.00, 10, 5, 'Cohort 1'),
(2, 'Jane Smith', 'janesmith@example.com', 80.00, 5, 10, 'Cohort 2'),
(3, 'Mike Tyson', 'miketyson@email.com', 30.00, 12, 15, 'Cohort 2'),
(4, 'John Cena', 'johncena@email.com', 20.00, 20, 20, 'Cohort 2');

-- --------------------------------------------------------

--
-- Table structure for table `weekly_attendance`
--

CREATE TABLE `weekly_attendance` (
  `id` int NOT NULL,
  `student_id` int DEFAULT NULL,
  `week` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `present` int NOT NULL,
  `absent` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- Dumping data for table `weekly_attendance`
--

INSERT INTO `weekly_attendance` (`id`, `student_id`, `week`, `present`, `absent`) VALUES
(1, 1, 'Week 1', 4, 1),
(2, 1, 'Week 2', 5, 0),
(3, 1, 'Week 3', 4, 1),
(4, 2, 'Week 1', 3, 2),
(5, 2, 'Week 2', 2, 3),
(6, 2, 'Week 3', 4, 1),
(7, 3, 'Week 1', 2, 3),
(8, 3, 'Week 2', 0, 5),
(9, 3, 'Week 3', 1, 4),
(10, 4, 'Week 1', 5, 0),
(11, 4, 'Week 2', 5, 0),
(12, 4, 'Week 3', 3, 2);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `weekly_attendance`
--
ALTER TABLE `weekly_attendance`
  ADD PRIMARY KEY (`id`),
  ADD KEY `student_id` (`student_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `students`
--
ALTER TABLE `students`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `weekly_attendance`
--
ALTER TABLE `weekly_attendance`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `weekly_attendance`
--
ALTER TABLE `weekly_attendance`
  ADD CONSTRAINT `weekly_attendance_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `students` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

    

#

4. Clone this repo. Insert your database URI to __database.yaml__ file, then install all the packages needed. In this project I'm using __flask__, __flask_cors__, __flask_mysqldb__, __Flask-SQLAlchemy__ & __psycopg2__:
    ```bash
    $ git clone https://github.com/LintangWisesa/CRUD_Flask_PostgreSQL.git
    $ cd CRUD_Flask_PostgreSQL
    $ pip install flask flask_cors Flask-SQLAlchemy psycopg2
    ```

#

5. Run the server file. Make sure your PostgreSQL server is still running. Your application server will run locally at __*http://localhost:5000/*__ :
    ```bash
    $ python app.py
    ```

#

6. Give a request to the server. You can use __Postman__ app:
    
    __See the opening screen (*home.html*)__
    ```bash
    GET /
    ```

    __Post a data to database:__ 
    ```bash
    POST /data
    body request: {name:"x", email:"y"}
    ```
    __Get all data & specific data by id:__
    ```bash
    GET /data
    GET /data/{:id}
    ```
    __Update a data by id__:
    ```bash
    PUT /data/{:id}
    body request: {name:"x", email:"y"}
    ```
    __Delete a data by id:__
    ```bash
    DELETE /data/{:id}
    ```

#

7. Enjoy your code! 😎👌
