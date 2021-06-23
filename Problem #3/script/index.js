const form = document.getElementById("register-form");

const validate = (key, value, data) => {
  switch (key) {
    case "email":
      if (value.indexOf("@") !== -1) {
        return [true, ""];
      } else {
        return [false, "รูปแบบอีเมลไม่ถูกต้อง"];
      }
    case "password":
      if (value.length < 8) {
        return [false, "รหัสผ่านต้องมีอย่างน้อย 8 ตัวอักษร"];
      } else {
        return [true, ""];
      }
    case "confirmpassword":
      if (value === data.password) {
        return [true, ""];
      } else {
        return [false, "รหัสผ่านไม่ตรงกัน"];
      }
    default:
      return [true, ""];
  }
};

form.addEventListener("submit", (event) => {
  event.preventDefault();
  const formData = new FormData(form);
  const data = {};
  let isDataValid = true;
  for (const [key, value] of formData.entries()) {
    data[key] = value;
    // Validate
    if (["email", "password", "confirmpassword"].includes(key)) {
      const [isValid, errorMessage] = validate(key, value, data);

      const input = document.getElementById(`${key}-input`);
      const helperText = document.getElementById(`${key}-helper-text`);

      if (isValid) {
        input.style.borderColor = "#d4d4d4";
        helperText.style.display = "none";
      } else {
        isDataValid = false;
        input.style.borderColor = "#ff5757";
        helperText.style.display = "block";
        helperText.innerText = errorMessage;
      }
    }
  }
  console.log(data);
  /* USER CODE Begin: What happened next after recieve form data (Optional) */

  /* USER CODE END: What happened next after recieve form data (Optional) */
});
