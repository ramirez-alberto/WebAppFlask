import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CancionListComponent } from './cancion-list.component';

describe('CancionListComponent', () => {
  let component: CancionListComponent;
  let fixture: ComponentFixture<CancionListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CancionListComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CancionListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
