import { HttpErrorResponse } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { RepositorioCancionesService } from 'src/app/shared/services/repositorio-canciones.service';
import { Cancion } from 'src/app/_interfaces/cancion.model';

@Component({
  selector: 'app-cancion-list',
  templateUrl: './cancion-list.component.html',
  styleUrls: ['./cancion-list.component.css']
})
export class CancionListComponent implements OnInit {
  canciones?: Cancion[];


  constructor(private repository: RepositorioCancionesService) { }

  ngOnInit(): void {
    this.getAllCanciones();
  }

  private getAllCanciones = () => {
    const apiUrl : string = 'canciones';
    this.repository.getCanciones(apiUrl).subscribe({
      next: (c: Cancion[]) => this.canciones = c,
      error: (err: HttpErrorResponse) => {console.log(err)}
    }
    )
  }

}
