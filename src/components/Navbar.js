import React from "react";
import "../App.css";
import $ from "jquery";
import "../responsive.css";

export default function Navbar() {
  $(function () {
    $(document).scroll(function () {
      var $nav = $(".fixed-top");
      $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
    });

    $(document).scroll(function () {
      var $nav1 = $(".navbar-nav.ml-auto");
      $nav1.toggleClass('scrolled', $(this).scrollTop() > $nav1.height());
    });

    $(document).scroll(function () {
      var $nav2 = $(".navbar-brand");
      $nav2.toggleClass('scrolled', $(this).scrollTop() > $nav2.height());
    });
  });

  return (
    <div class="App">
      <nav class="navbar navbar-expand-md navbar-custom fixed-top pr-4">
      <a class="navbar-brand"><img src={require("../images/SULogo.png")} class="img-fluid" height="40" width="40" />&nbsp; Swift UnderGrads</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#collapsibleNavbar">
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="collapsibleNavbar">  
          <ul class="navbar-nav ml-auto">
            <li class="nav-item"><a class="nav-link" href="/">Home</a></li>
            <li class="nav-item"><a class="nav-link" href="/about">About</a></li>

            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" id="navbardrop" data-toggle="dropdown">Notes</a>
              <div class="dropdown-menu" id="dropbg">
                <a class="dropdown-item" href="/enggnotes">Engineering</a>
                <a class="dropdown-item" href="/pharmnotes">Pharmacy</a>
              </div>
            </li>
            <li class="nav-item"><a class="nav-link" href="/contact">Contact</a></li>
          </ul>
        </div>
      </nav>
    </div>
  );
}
