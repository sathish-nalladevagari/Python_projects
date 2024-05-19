function validate(values, rules) {
    const errors = {};
    let isValid = true;
  
    for (const field in rules) {
      const rule = rules[field];
  
      if (rule.required && !values[field]) {
        errors[field] = `${field} is required`;
        isValid = false;
      }
  
      if (field === 'email' && values[field]) {
        const re = /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i;
        if (!re.test(values[field])) {
          errors.email = 'Invalid email address';
          isValid = false;
        }
      }
  
      if (field === 'confirmPassword' && values.password) {
        if (values[field] !== values.password) {
          errors.confirmPassword = 'Passwords do not match';
          isValid = false;
        }
      }
  
      if (rule.minLength && values[field] && values[field].length < rule.minLength) {
        errors[field] = `${field} must be at least ${rule.minLength} characters`;
        isValid = false;
      }
  
      if (rule.maxLength && values[field] && values[field].length > rule.maxLength) {
        errors[field] = `${field} must be at most ${rule.maxLength} characters`;
        isValid = false;
      }
  
      if (rule.pattern && values[field] && !rule.pattern.test(values[field])) {
        errors[field] = `${field} is invalid`;
        isValid = false;
      }
    }
  
    if (isValid) {
      return { success: 'Form is valid' };
    }
  
    return errors;
  }
  

  const rules = {
    email: {
      required: true,
    },
    password: {
      required: true,
      minLength: 8,
    },
    confirmPassword: {
      required: true,
      minLength: 8,
    },
  };
  
  const values = {
    email: 'test@example.com',
    password: 'password',
    confirmPassword: 'password',
  };
  
  const result = validate(values, rules);
  console.log(result);