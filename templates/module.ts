import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { SharedModule } from '../../shared/shared.module';
import { $COMPONENT_NAME$ } from '$COMPONENT_PATH$';
import { $ROUTE_NAME$ } from '$ROUTE_PATH$';

@NgModule({
  declarations: [$COMPONENT_NAME$],
  imports: [SharedModule, RouterModule.forChild($ROUTE_NAME$)],
})
export class $MODULE_NAME$ {}
