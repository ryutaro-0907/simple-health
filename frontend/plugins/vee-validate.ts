import { localize } from 'vee-validate';
import en from 'vee-validate/dist/locale/en.json';
import ja from 'vee-validate/dist/locale/ja.json';
import customEn from '~/locales/en';
import customJa from '~/locales/ja';

localize({ en, ja });
// @ts-ignore
localize('en', customEn);
// @ts-ignore
localize('ja', customJa);
