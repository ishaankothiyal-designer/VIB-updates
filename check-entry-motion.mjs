import assert from 'node:assert/strict';
import {createRequire} from 'node:module';
const require=createRequire(import.meta.url);
const {registrationState}=require('./dist/vehicle-entry.js');
assert.deepEqual(registrationState(' dl 03 ab 1234 '),{valid:true,value:'DL03AB1234'});
assert.equal(registrationState('22 BH 1234 AA').valid,true);
for(const value of ['', 'ABCDEF', '12345678','DL<03>AB1234','DL03','A'.repeat(100)]) assert.equal(registrationState(value).valid,false,value);
console.log('PASS: registration normalization and invalid input.');
