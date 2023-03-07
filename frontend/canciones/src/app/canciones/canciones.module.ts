import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CancionListComponent } from './cancion-list/cancion-list.component';



@NgModule({
  declarations: [

    CancionListComponent
  ],
  imports: [
    CommonModule
  ],
  exports: [CancionListComponent]
})
export class CancionesModule { }
