"""empty message

Revision ID: 6ba817e3d6f0
Revises: 0a850687a0fe
Create Date: 2021-04-07 15:19:19.937405

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ba817e3d6f0'
down_revision = '0a850687a0fe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shows', sa.Column('artist_image_link', sa.String(length=500), nullable=True))
    op.add_column('shows', sa.Column('artist_name', sa.String(), nullable=False))
    op.add_column('shows', sa.Column('venue_name', sa.String(), nullable=False))
    op.create_foreign_key(None, 'shows', 'Artist', ['artist_image_link'], ['image_link'])
    op.create_foreign_key(None, 'shows', 'Artist', ['artist_name'], ['name'])
    op.create_foreign_key(None, 'shows', 'Venue', ['venue_name'], ['name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'shows', type_='foreignkey')
    op.drop_constraint(None, 'shows', type_='foreignkey')
    op.drop_constraint(None, 'shows', type_='foreignkey')
    op.drop_column('shows', 'venue_name')
    op.drop_column('shows', 'artist_name')
    op.drop_column('shows', 'artist_image_link')
    # ### end Alembic commands ###
