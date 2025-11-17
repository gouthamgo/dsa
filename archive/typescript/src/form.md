// Interfaces and Types
interface FormData {
  email: string;
  password: string;
  age: number;
}

type ValidationRule<T> = (value: T) => string | null;

// Reusable Validation Rules
const required = (value: string | number): string | null =>
  value ? null : "This field is required.";

const regex = (pattern: RegExp, errorMessage: string) => (value: string): string | null =>
  pattern.test(value) ? null : errorMessage;

const minLength = (length: number) => (value: string): string | null =>
  value.length >= length ? null : `Must be at least ${length} characters long.`;

const minValue = (min: number) => (value: number): string | null =>
  value >= min ? null : `Must be at least ${min}.`;

// Validation Rules for Each Field
const validationRules: Record<keyof FormData, ValidationRule<any>[]> = {
  email: [required, regex(/^\S+@\S+\.\S+$/, "Must be a valid email address.")],
  password: [required, minLength(8)],
  age: [required, minValue(18)],
};

// Validation Function
function validateForm(data: FormData): Record<string, string[]> {
  const errors: Record<string, string[]> = {};

  for (const field in data) {
    const value = data[field as keyof FormData];
    const rules = validationRules[field as keyof FormData];

    const fieldErrors = rules.map((rule) => rule(value)).filter((error) => error !== null) as string[];

    if (fieldErrors.length > 0) {
      errors[field] = fieldErrors;
    }
  }

  return errors;
}

// Test Data
const formData: FormData = {
  email: "invalid-email",
  password: "123",
  age: 16,
};

console.log(validateForm(formData));
