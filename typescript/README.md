# 1. Create a new directory for your project
mkdir my-typescript-project-template
cd my-typescript-project-template

# 2. Initialize a new npm project
npm init -y

# 3. Install TypeScript, tsc-watch, and nodemon as dev dependencies
npm install typescript tsc-watch nodemon --save-dev

# 4. Create a tsconfig.json file and configure it
npx tsc --init
# Then, edit tsconfig.json to match the following:
# {
#   "compilerOptions": {
#     "target": "es6",
#     "module": "commonjs",
#     "outDir": "./dist",
#     "strict": true,
#     "esModuleInterop": true,
#     "skipLibCheck": true,
#     "forceConsistentCasingInFileNames": true
#   },
#   "include": ["src/**/*"]
# }

# 5. Create a nodemon.json file and configure it
touch nodemon.json
# Then, edit nodemon.json to match the following:
# {
#   "watch": ["dist"],
#   "ext": "js",
#   "exec": "node dist/index.js"
# }

# 6. Create a src directory and an index.ts file
mkdir src
touch src/index.ts
# Then, edit src/index.ts and add some sample code:
# let message: string = "Hello Template";
# console.log(message);

# 7. Create a README.md file and add template documentation
touch README.md
# Then, edit README.md and add the markdown content from the previous response.

# 8. Run tsc-watch to start the development environment
npx tsc-watch --onSuccess "npx nodemon"

# If you want to use the template for a new project:

# 1. Clone the template repository (replace <your-template-repository-url>)
# git clone <your-template-repository-url> your-new-project
# cd your-new-project

# 2. Install dependencies
# npm install

# 3. Start development
# npx tsc-watch --onSuccess "npx nodemon"