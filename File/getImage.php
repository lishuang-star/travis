<?php
global $time_start;
$time_start = microtime(true);
function testTime($line){
    global $time_start;
    $time_end = microtime(true);
    $time = $time_end - $time_start;
    if ($time > 1) {
        error_log(__FILE__." ".$line . 'Execution time : ' . $time . ' seconds');
    }
    $time_start = microtime(true);
}
function fileOlderThen($file, $ageInSeconds){
    $filemtime = @filemtime($file);  // returns FALSE if file does not exist
    if(!$filemtime || (time() - $filemtime >= $ageInSeconds)){
        return true;
    }
    return false;
}

testTime(__LINE__);

require_once dirname(__FILE__) . '/../videos/configuration.php';
header('Access-Control-Allow-Origin: *');

//获取url，对url进行base64解码，赋值给url变量。
$url = base64_decode($_GET['base64Url']);

// 进行黑名单过滤
 // Set blacklist 
$substitutions = array( 
        ';'  => '', 
        '| ' => '', 
        '-'  => '', 
        '$'  => '', 
        '('  => '', 
        ')'  => '', 
        '`'  => '', 
        '||' => '', 
    ); 
	
$url = str_replace( array_keys( $substitutions ), $substitutions, $url ); 

$destinationFile = md5($url);
$destination = sys_get_temp_dir().DIRECTORY_SEPARATOR.$destinationFile;
$destinationPallet = "{$destination}palette.png";
$cache_life = '600'; //caching time, in seconds
$ob_flush = false;

testTime(__LINE__);

//根据format参数不同，进行处理。拼接$exec变量
if($_GET['format'] === 'png'){
    header('Content-Type: image/x-png');
    $destination .= ".".$_GET['format'];
	
	#把视频的前1帧转换成一张400x225尺寸大小的，格式为jpg的图片 
	#待转换的视频地址由$url变量值提供。这里的$url值可以通过GET变量传入，而未经过任何过滤
    $exec = "ffmpeg -i {$url} -f image2  -s 400x225 -vframes 1 -y {$destination}";
    $destinationTmpFile = "{$global['systemRootPath']}view/img/OnAir.png";
}else if($_GET['format'] === 'jpg'){
    header('Content-Type: image/jpg');
    $destination .= ".".$_GET['format'];
    $exec = "ffmpeg -i {$url} -f image2  -s 400x225 -vframes 1 -y {$destination}";
    $destinationTmpFile = "{$global['systemRootPath']}view/img/OnAir.jpg";
}else if($_GET['format'] === 'gif'){
    // gif image has the double lifetime
    $cache_life*=2;
    header('Content-Type: image/gif');
    $destination .= ".".$_GET['format'];    
    //Generate a palette:
    $ffmpegPallet ="ffmpeg -y -t 3 -i {$url} -vf fps=10,scale=320:-1:flags=lanczos,palettegen {$destinationPallet}";
    $exec ="ffmpeg -y -t 3 -i {$url} -i {$destinationPallet} -filter_complex \"fps=10,scale=320:-1:flags=lanczos[x];[x][1:v]paletteuse\" {$destination}";
    $destinationTmpFile = "{$global['systemRootPath']}view/img/notfound.gif";
}else{
    error_log("ERROR Destination get Image {$_GET['format']} not suported");
    die();
}

testTime(__LINE__);

if(!is_readable($destination)){
    echo url_get_contents($destinationTmpFile);
    error_log("Destination get Temp Image {$_GET['format']}: {$destinationTmpFile}");
}else{
    // flush old image then encode
    echo url_get_contents($destination);
    error_log("Destination get Image {$_GET['format']}: {$destination}");
}

testTime(__LINE__);

ob_flush();


// 在format=png的时候 $fmpegPallet为空 所以执行else后的语句
if(!file_exists($destination) || fileOlderThen($destination, $cache_life) || !empty($_GET['renew'])){
    if(!empty($ffmpegPallet)){        
        $cmd = "{$ffmpegPallet} &> /dev/null &";        
        exec($cmd);
        error_log("Create Gif Pallet: {$cmd}");        
        if(is_readable($destinationPallet)){
            $cmdGif = "{$exec} &> /dev/null &";
            exec($cmdGif);
            error_log("Create Gif with Ppallet: {$cmd}");
        }else{
            $cmdGif = "ffmpeg  -y -t 3 -i {$url} -vf fps=10,scale=320:-1 {$destination} &> /dev/null &";
            exec($cmdGif);
            error_log("Create Gif no Pallet: {$cmd}");
        }
    }else{
        $cmd = "{$exec} &> /dev/null &";
        //通过`exec方法`将`$cmd`变量中的内容执行,
		exec($cmd);
        error_log("Exec get Image: {$cmd}");
    }
}else{
    
}
testTime(__LINE__);
die();