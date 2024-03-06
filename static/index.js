window.onload = function () {
  const btn = document.getElementById("button");
  document
    .getElementById("contact-form")
    .addEventListener("submit", function (event) {
      event.preventDefault();
      var myForm = document.getElementById("contact-form");
      console.log("on est la");
      btn.value = "Predict en cours...";

      function submit_entry() {
        var result_p = document.getElementById("result_p");
        var age = document.getElementById("age");
        var height = document.getElementById("height");
        var weight = document.getElementById("weight");
        var pregnancies = document.getElementById("pregnancies");
        var glucose = document.getElementById("glucose");
        var blood_pressure = document.getElementById("blood_pressure");
        var skin_thickness = document.getElementById("skin_thickness");
        var insuline = document.getElementById("insuline");
        var grandparent_diabetes = document.getElementById(
          "grandparent_diabetes"
        );
        if (grandparent_diabetes.checked) {
          grandparent_diabetes.value = "1";
        } else {
          grandparent_diabetes.value = "0";
        }
        var parent_diabetes = document.getElementById("parent_diabetes");
        if (parent_diabetes.checked) {
          parent_diabetes.value = "1";
        } else {
          parent_diabetes.value = "0";
        }
        var sibling_diabetes = document.getElementById("sibling_diabetes");
        if (sibling_diabetes.checked) {
          sibling_diabetes.value = "1";
        } else {
          sibling_diabetes.value = "0";
        }

        var entry = {
          age: age.value,
          height: height.value,
          weight: weight.value,
          pregnancies: pregnancies.value,
          glucose: glucose.value,
          blood_pressure: blood_pressure.value,
          skin_thickness: skin_thickness.value,
          insuline: insuline.value,
          grandparent_diabetes: grandparent_diabetes.value,
          parent_diabetes: parent_diabetes.value,
          sibling_diabetes: sibling_diabetes.value,
        };

        fetch(`${window.location}getpredict`, {
          method: "POST",
          credentials: "include",
          body: JSON.stringify(entry),
          cache: "no-cache",
          headers: new Headers({ "content-type": "application/json" }),
        }).then(function (response) {
          if (response.status !== 200) {
            console.log(`response status was not 200 : ${response.status}`);
          }
          response.json().then(function (data) {
            //mettre a jour le p
            result_p.innerText = data.message;
          });
        });
      }
      btn.value = "Predict";

      submit_entry();
    });
};
