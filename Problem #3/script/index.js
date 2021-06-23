const form = document.getElementById("register-form");

const validate = (key, value, data) => {
  if (key === "email") {
    if (value == "") {
      return [false, "โปรดระบุอีเมล"];
    }
    if (value.indexOf("@") === -1) {
      return [false, "รูปแบบอีเมลไม่ถูกต้อง"];
    }
  } else if (key === "password") {
    if (value.length < 8) {
      return [false, "รหัสผ่านต้องมีอย่างน้อย 8 ตัวอักษร"];
    }
  } else if (key === "confirmpassword") {
    if (value !== data.password) {
      return [false, "รหัสผ่านไม่ตรงกัน"];
    }
  } else if (key === "name") {
    if (value === "") {
      return [false, "โปรดระบุชื่อ"];
    }
  } else if (key === "lastname") {
    if (value === "") {
      return [false, "โปรดระบุนามสกุล"];
    }
  } else if (key === "username") {
    if (value === "") {
      return [false, "โปรดระบุชื่อผู้ใช้"];
    }
  }
  return [true, ""];
};

form.addEventListener("submit", (event) => {
  event.preventDefault();
  const formData = new FormData(form);
  const data = {};
  let isDataValid = true;
  for (const [key, value] of formData.entries()) {
    data[key] = value;
    // Validate
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
  console.log(data);
  /* USER CODE Begin: What happened next after recieve form data (Optional) */

  /* USER CODE END: What happened next after recieve form data (Optional) */
});
