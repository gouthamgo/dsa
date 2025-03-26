interface FormData{
    email:string;
    password:string;
    age:number
}


type ValidationRule<T> = (value: T) => string | null ;


const required = (value: string | number): string |null => 
    value ? null : "This field is needed"



const regex = (pattern: RegExp, errorMessage: string) => (value: string): string | null =>
    pattern.test(value) ? null : errorMessage;



const minLength = (length: number) => (value:string):string| null => value.length >= length ? null : ''


