<?php header('X-Powered-By: LISP Web Engine'); header("server: none");?>
<html>

<head>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
    <script src="assets/js/materialize.js"></script>
    <!--Start of Tawk.to Script-->
    <script type="text/javascript">
        var Tawk_API = Tawk_API || {},
            Tawk_LoadStart = new Date();
        (function() {
            var s1 = document.createElement("script"),
                s0 = document.getElementsByTagName("script")[0];
            s1.async = true;
            s1.src = 'https://embed.tawk.to/56c723aa06613232645d2a3a/default';
            s1.charset = 'UTF-8';
            s1.setAttribute('crossorigin', '*');
            s0.parentNode.insertBefore(s1, s0);
        })();
    </script>
    <?php session_start(); $_SESSION['csrf_token'] = base64_encode(openssl_random_pseudo_bytes(32)); echo "<script>"; echo 'var token = "'.$_SESSION[ 'csrf_token']. '"'; echo "</script>"; ?>
    <!--End of Tawk.to Script-->
    <link rel="stylesheet" href="assets/css/materialize.css">
    <link href="http://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <link rel="shortcut icon" type="image/png" href="assets/img/favicon.png" />
    <link rel="stylesheet" href="assets/css/style.css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>SchedStalk v2016.1B</title>
</head>
<script>
    $(document).ready(function() {
        // the "href" attribute of .modal-trigger must specify the modal ID that wants to be triggered
        $('.modal-trigger').leanModal();
    });
</script>

<body>
    <nav>
        <div class="nav-wrapper light-green accent-4">
            <a href="#" data-activates="mobile-demo" class="button-collapse"><i class="material-icons">menu</i></a>
            <ul class="right hide-on-med-and-down">
                <li>
                    <!-- Modal Trigger -->
                    <a class="modal-trigger" href="#modal1">About</a>

                    <!-- Modal Structure -->
                    <div id="modal1" class="modal black-text modal-fixed-footer">
                        <div class="modal-content">
                            <h4>About</h4>
                            <p class="flow-text">
                                <h6>Schedstalk merupakan mesin pencarian yang dapat menjawab pertanyaan-pertanyaan dalam bentuk bahasa natural. Pertanyaan yang dapat dijawab oleh schedstalk meliputi pertanyaan-pertanyaan tentang kelas-kelas ataupun mata kuliah yang diambil oleh mahasiswa IPB.</h6>
                                <h6>Merupakan produk riset dari salah satu mahasiswa ilmu komputer IPB angkatan 2012 untuk projek akhir mata kuliah Information Retrieval.</h6>
                            </p>

                        </div>
                        <div class="modal-footer">
                            <a href="#!" class=" modal-action modal-close waves-effect waves-green btn-flat">Close</a>
                        </div>
                    </div>
                </li>
                <li>
                    <!-- Modal Trigger -->
                    <a class="modal-trigger" href="#modal2">FAQ</a>

                    <!-- Modal Structure -->
                    <div id="modal2" class="modal black-text">
                        <div class="modal-content">
                            <h6>
             
              <ul>
               
               <li>Q : WTF is this ?</li> <br/>
               <li>A : Baca laman about.</li><br/>
               <li>Q : gratis ?</li> <br/>
               <li>A : y.</li><br/>
               <li>Q : bayar ?</li><br/> 
               <li>A : g.</li><br/>
               <li>Q : waw</li> <br/>
               <li>A : ?.</li><br/>
                </ul>
               
        </h6>
                        </div>
                        <div class="modal-footer">
                            <a href="#!" class=" modal-action modal-close waves-effect waves-green btn-flat">CLose</a>
                        </div>
                    </div>
                </li>
                <li>
                    <!-- Modal Trigger -->
                    <a class="modal-trigger" href="#modal3">How to use?</a>

                    <!-- Modal Structure -->
                    <div id="modal3" class="modal modal-fixed-footer black-text">
                        <div class="modal-content">
                            <h4>How to use?</h4>
                            <h6 class="black-text">
              <p class="flow-text">
                   <a href="https://drive.google.com/file/d/0B_kAnrNjT4xeNUp1eExXOEtIMHc/view?usp=sharing" target="_blank">Download contoh penggunaan</a><br/><a href="https://docs.google.com/document/d/1e9qbDVBW3jgcekgT8cTdmcOmBNI1uD12_g4fSsMcA_Q/pub" target="_blank">Baca online</a>
        </h6>
                        </div>
                        <div class="modal-footer">
                            <a href="#!" class=" modal-action modal-close waves-effect waves-green btn-flat">Close</a>
                        </div>
                    </div>
                </li>
            </ul>
            <ul class="side-nav" id="mobile-demo">
                <li><a href=".">Home</a>
                </li>
                <li><a href="about.html">About</a>
                </li>
                <li><a href="faq.html">FAQ</a>
                </li>
                <li><a href="htu.html">How to use?</a>
                </li>
            </ul>
        </div>
    </nav>
    <div class="center">
        <a href="#"><img id="logo" class="responsive-img" src="assets/img/logo.png" onclick="location.reload();" />
        </a>

        <div class="row">
            <div id="input_field" class="input-field col s12 m12">
                <input id="search_query" type="text" class="validate" name="q">
                <label for="search_query">Apa yang kamu cari ?</label>
            </div>
            <button id="stalk_button" style="margin-top:15px;" class="btn waves-light light-green accent-4" type="submit" name="action">stalk<i class="material-icons right">visibility</i>
            </button>
            <img id="loading" src="assets/img/loading.gif" />
        </div>
        <div class="row">
            <div class="col s1">&nbsp;</div>
            <div class="col s10">
                <div id="result" class="card light-green accent-1">
                    <p id="resultString"></p>
                </div>

            </div>
            <div class="col s1">&nbsp;</div>
        </div>

        <footer class="page-footer light-green accent-4">
            <div class="footer-copyright">
                <div class="container">
                    Project Schedstalk &copy; 2016
                </div>
            </div>
        </footer>
</body>
<script src="assets/js/flow.js"></script>

</html>