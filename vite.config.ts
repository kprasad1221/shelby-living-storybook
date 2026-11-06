import {defineConfig} from "vite";
import {fileURLToPath} from "node:url";
export default defineConfig({server:{host:"0.0.0.0",allowedHosts:["terminal.local"]},esbuild:{jsx:"automatic"},resolve:{alias:[{find:"@designcodeio/threeui/style.css",replacement:fileURLToPath(new URL("./baseline/src/shaders/threeui.css",import.meta.url))},{find:"@designcodeio/threeui",replacement:fileURLToPath(new URL("./src/threeui-entry.tsx",import.meta.url))}]}});
