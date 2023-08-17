# boostng: :rocket: Scripts for speeding up development with angular

You can use boostng to generate a template Angular compnent entirely compatible to JHipster.

In order to install the script run
```shell
pip install boostng
```

Just start the script in the parent/target directory:
```shell
boostng
```

You will be asked to enter the components name. The name should be like this: parent-name (e.g. stock-list)

Afterwards the script will generate the following content:

```
├── name
│   ├── parent-name.component.html
│   ├── parent-name.component.css
│   ├── parent-name.component.ts
│   ├── parent-name.module.ts
│   ├── parent-name.route.ts
```
