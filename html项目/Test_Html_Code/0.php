<?php
if(isset($_FILES['file'])) {
$file = $_FILES['file'];
$file_name = $file['name'];
$file_tmp = $file['tmp_name'];
$file_size = $file['size'];
$file_error = $file['error'];
$file_ext = strtolower(end(explode('.', $file_name)));

$allowed = array('txt', 'pdf', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx');

if(in_array($file_ext, allowed)) { if(file_error === 0) {
if($file_size <= 2097152) {
$file_name_new = uniqid('', true) . '.' . $file_ext;
$file_destination = 'uploads/' . $file_name_new;

    if(move_uploaded_file($file_tmp, $file_destination)) {
      echo '文件上传成功！';
    }
  } else {
    echo '文件过大！';
  }
} else {
  echo '上传文件出错！';
}
} else {
echo '文件类型不支持！';
}
}
?>