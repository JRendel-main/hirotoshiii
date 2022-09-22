<?php
	if(ISSET($_GET['id'])){
		require_once 'connection.php';
		$id = $_GET['id'];
		$sql = $conn->prepare("DELETE from `member` WHERE `mem_id`='$id'");
		$sql->execute();
		header('location:index.php');
	}
?>