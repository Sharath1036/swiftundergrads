import React from "react";
import "../App.css";
import "../responsive.css";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";

export default function Contact() {
  return (
    <div>
      <div class="container-fluid bg7">
        <Navbar />
        <br /><br /><br /><br /><br /><br /><br/><br/>
        <div class="jumbotron bg-transparent align-items-center mx-auto d-block">
          <h1 align="center" class="text-white">Contact Page</h1>
        </div>
      </div>

      <div class="container">
        <h2 class="mt-5">Contact Us</h2>
        <p>Fill out the form so that we can reach out to you...</p>
        <form action="/action_page.php" class="needs-validation" novalidate>

          <div class="form-group">
            <label for="uname">Full Name:</label>
            <input type="text" class="form-control" id="uname" placeholder="Enter Name" name="uname" required/>
            <div class="valid-feedback">Valid.</div>
            <div class="invalid-feedback">Please fill out this field.</div>
          </div>

          <div class="form-group">
            <label for="contact">Email ID:</label>
            <input type="text" class="form-control" id="pwd" placeholder="Enter Email ID" name="email" required />
            <div class="valid-feedback">Valid.</div>
            <div class="invalid-feedback">Please fill out this field.</div>
          </div>

          <div class="form-group">
            <label for="contactno">Contact Number:</label>
            <input type="text" class="form-control" id="pwd" placeholder="Enter Contact Number" name="contactno" required />
            <div class="valid-feedback">Valid.</div>
            <div class="invalid-feedback">Please fill out this field.</div>
          </div>

          <div class="form-group">
            <label for="comment">Reason for contacting:</label>
            <textarea class="form-control" rows="5" id="comment" name="text"></textarea>
        </div> 

          <div class="form-group form-check">
            <label class="form-check-label">
              <input class="form-check-input" type="checkbox" name="remember" required />{" "}I agree that all the information is true.
              <div class="valid-feedback">Valid.</div>
              <div class="invalid-feedback">Check this checkbox to continue.</div>
            </label>
          </div>
          <button type="submit" class="btn btn-primary">Submit</button>
        </form>
      </div>
      <div class="mgn"><Footer /></div>
    </div>
  );
}
