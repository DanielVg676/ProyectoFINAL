-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 12, 2024 at 04:20 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bd_pacific`
--

-- --------------------------------------------------------

--
-- Table structure for table `clientes`
--

CREATE TABLE `clientes` (
  `id` int(10) NOT NULL,
  `usuario` int(16) NOT NULL,
  `contrasena` varchar(20) NOT NULL,
  `nombre` varchar(40) NOT NULL,
  `direccion` varchar(100) NOT NULL,
  `telefono` varchar(10) NOT NULL,
  `email` varchar(30) NOT NULL,
  `ocupacion` varchar(30) NOT NULL,
  `historial` varchar(300) NOT NULL,
  `saldo` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `clientes`
--

INSERT INTO `clientes` (`id`, `usuario`, `contrasena`, `nombre`, `direccion`, `telefono`, `email`, `ocupacion`, `historial`, `saldo`) VALUES
(1, 120, '120', 'Cristian V', 'Colinas del saltito 325', '6182066613', 'cris022@gmail.com', 'maestro', '14208', 2000000),
(2, 183147, '7c9e7c1494b2684ab7c1', 'pepe ramirez', 'la zapata', '61829011', 'pepe@gmail.com', 'maestro', '', 5000),
(3, 321, '8d23cf6c86e834a7aa6e', 'daniel', 'valle', '6181563424', 'dv9565', 'empleado', '', 2000),
(4, 654, '92a6a32f99def322d70e', 'daniel', 'valle', '6181563424', 'dv9565', 'conserje', '', 4000),
(5, 321, '8d23cf6c86e834a7aa6e', 'daniel', 'asdasdas', '2342342', 'asdasd', 'empleado', '', 2000),
(6, 131313, '131313', 'ALAMBRITO', 'TEJERINGO', '6181563424', 'DCDS', 'psicologo', '', 5000),
(7, 453, 'd83c7ee736be931d85b7', 'elba nana nita', 'zona media', '6181563424', 'sadcas', 'astronauta', '', 5000000),
(8, 454546, 'a55e3cf3331a74219d4b', 'elbalaso', '20 de noviembre', '61856745', 'sadasf', 'abogada', '', 2000),
(9, 9685, 'c83e0fc471e3faf8daf9', 'elsapato', '20 de noviembre', '6181563424', 'sadsad', 'empleado', '', 2000),
(10, 6474, '32037f51f7c37b9e660a', 'Tonny strak', 'Torre de los vengadores', '6181563424', 'tonnybbQgmail.com', 'dios', '', 2000000);

-- --------------------------------------------------------

--
-- Table structure for table `empleados`
--

CREATE TABLE `empleados` (
  `ID` int(11) NOT NULL,
  `usuario` int(16) DEFAULT NULL,
  `contrasena` varchar(20) DEFAULT NULL,
  `nombre` varchar(40) DEFAULT NULL,
  `direccion` varchar(100) DEFAULT NULL,
  `telefono` varchar(10) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `salario` float DEFAULT NULL,
  `puesto` varchar(20) DEFAULT NULL,
  `id_banco` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `empleados`
--

INSERT INTO `empleados` (`ID`, `usuario`, `contrasena`, `nombre`, `direccion`, `telefono`, `email`, `salario`, `puesto`, `id_banco`) VALUES
(3, 987, '987', 'Daniel Contreras', 'valle de suchil', '6181563424', 'dv956543', 20000, 'empleado', NULL),
(4, 789, '789', 'empleadonormal', 'valle', '6182341212', 'dcdsada', 2000, 'conserje', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `prestamos`
--

CREATE TABLE `prestamos` (
  `id_prestamo` int(10) NOT NULL,
  `id_cliente` int(10) NOT NULL,
  `permiso_prestamo` tinyint(1) NOT NULL,
  `id_transaccion` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `prestamos`
--

INSERT INTO `prestamos` (`id_prestamo`, `id_cliente`, `permiso_prestamo`, `id_transaccion`) VALUES
(1, 1, 1, 1),
(2, 1, 0, 1),
(3, 1, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `retiros`
--

CREATE TABLE `retiros` (
  `id_retiro` int(10) NOT NULL,
  `id_cliente` int(10) NOT NULL,
  `monto` float NOT NULL,
  `id_transaccion` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `retiros`
--

INSERT INTO `retiros` (`id_retiro`, `id_cliente`, `monto`, `id_transaccion`) VALUES
(1, 1, 300, 1),
(2, 2, 500, 2),
(3, 3, 2000, 3);

-- --------------------------------------------------------

--
-- Table structure for table `transacciones`
--

CREATE TABLE `transacciones` (
  `id_transaccion` int(10) NOT NULL,
  `descripcion` varchar(50) NOT NULL,
  `fecha` date NOT NULL,
  `monto` float NOT NULL,
  `id_cliente` int(10) NOT NULL,
  `id_banco` int(10) DEFAULT NULL,
  `tipo` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `transacciones`
--

INSERT INTO `transacciones` (`id_transaccion`, `descripcion`, `fecha`, `monto`, `id_cliente`, `id_banco`, `tipo`) VALUES
(1, 'para mamá', '2024-08-08', 300, 3, NULL, 'transferencia'),
(2, 'para pepitp', '2024-08-08', 100, 1, NULL, 'transferencia'),
(3, 'para pepito', '2024-08-08', 1200, 1, NULL, 'transferencia'),
(4, 'para pepito', '2024-08-08', 2, 1, NULL, 'transferencia'),
(5, 'para pepto', '2024-08-08', 200, 1, NULL, 'transferencia'),
(6, 'para pepito', '2024-08-08', 200, 1, NULL, 'transferencia'),
(7, 'para pepito', '2024-08-08', 300, 1, NULL, 'transferencia'),
(8, 'para pepito', '2024-08-08', 100, 1, NULL, 'transferencia');

-- --------------------------------------------------------

--
-- Table structure for table `transferencias`
--

CREATE TABLE `transferencias` (
  `id_transferencia` int(10) NOT NULL,
  `id_emisor` int(10) NOT NULL,
  `usuario_destino` int(16) NOT NULL,
  `banco_destino` int(10) NOT NULL,
  `impuesto` float NOT NULL,
  `id_transaccion` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `transferencias`
--

INSERT INTO `transferencias` (`id_transferencia`, `id_emisor`, `usuario_destino`, `banco_destino`, `impuesto`, `id_transaccion`) VALUES
(1, 1, 183147, 1, 30, 1),
(2, 1, 183147, 1, 30, 2),
(3, 1, 183147, 1, 30, 3),
(4, 1, 183147, 1, 30, 4),
(5, 1, 183147, 1, 30, 5),
(6, 1, 183147, 1, 30, 6),
(7, 1, 183147, 1, 30, 7);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `empleados`
--
ALTER TABLE `empleados`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `prestamos`
--
ALTER TABLE `prestamos`
  ADD PRIMARY KEY (`id_prestamo`),
  ADD KEY `id_cliente` (`id_cliente`),
  ADD KEY `id_transaccion` (`id_transaccion`);

--
-- Indexes for table `retiros`
--
ALTER TABLE `retiros`
  ADD PRIMARY KEY (`id_retiro`),
  ADD KEY `id_cliente` (`id_cliente`),
  ADD KEY `id_transaccion` (`id_transaccion`);

--
-- Indexes for table `transacciones`
--
ALTER TABLE `transacciones`
  ADD PRIMARY KEY (`id_transaccion`),
  ADD KEY `id_cliente` (`id_cliente`);

--
-- Indexes for table `transferencias`
--
ALTER TABLE `transferencias`
  ADD PRIMARY KEY (`id_transferencia`),
  ADD KEY `id_transaccion` (`id_transaccion`),
  ADD KEY `id_emisor` (`id_emisor`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `clientes`
--
ALTER TABLE `clientes`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `empleados`
--
ALTER TABLE `empleados`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `prestamos`
--
ALTER TABLE `prestamos`
  MODIFY `id_prestamo` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `retiros`
--
ALTER TABLE `retiros`
  MODIFY `id_retiro` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `transacciones`
--
ALTER TABLE `transacciones`
  MODIFY `id_transaccion` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `transferencias`
--
ALTER TABLE `transferencias`
  MODIFY `id_transferencia` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `prestamos`
--
ALTER TABLE `prestamos`
  ADD CONSTRAINT `prestamos_ibfk_1` FOREIGN KEY (`id_cliente`) REFERENCES `clientes` (`id`),
  ADD CONSTRAINT `prestamos_ibfk_2` FOREIGN KEY (`id_transaccion`) REFERENCES `transacciones` (`id_transaccion`);

--
-- Constraints for table `retiros`
--
ALTER TABLE `retiros`
  ADD CONSTRAINT `retiros_ibfk_1` FOREIGN KEY (`id_cliente`) REFERENCES `clientes` (`id`),
  ADD CONSTRAINT `retiros_ibfk_2` FOREIGN KEY (`id_transaccion`) REFERENCES `transacciones` (`id_transaccion`);

--
-- Constraints for table `transacciones`
--
ALTER TABLE `transacciones`
  ADD CONSTRAINT `transacciones_ibfk_1` FOREIGN KEY (`id_cliente`) REFERENCES `clientes` (`id`);

--
-- Constraints for table `transferencias`
--
ALTER TABLE `transferencias`
  ADD CONSTRAINT `transferencias_ibfk_1` FOREIGN KEY (`id_emisor`) REFERENCES `clientes` (`id`),
  ADD CONSTRAINT `transferencias_ibfk_2` FOREIGN KEY (`id_transaccion`) REFERENCES `transacciones` (`id_transaccion`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
