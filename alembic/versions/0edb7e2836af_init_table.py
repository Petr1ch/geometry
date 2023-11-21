"""Init table

Revision ID: 0edb7e2836af
Revises: 
Create Date: 2023-11-21 18:18:10.292377

"""
import geoalchemy2
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0edb7e2836af'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('fields',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('crop', sa.String(), nullable=True),
    sa.Column('productivity', sa.Float(), nullable=True),
    sa.Column('area_ha', sa.Float(), nullable=True),
    sa.Column('history', sa.String(), nullable=True),
    sa.Column('region', sa.String(), nullable=True),
    sa.Column('score', sa.String(), nullable=True),
    sa.Column('geometry', geoalchemy2.types.Geometry(geometry_type='POLYGON', from_text='ST_GeomFromEWKT', name='geometry'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('fields')
    # ### end Alembic commands ###
