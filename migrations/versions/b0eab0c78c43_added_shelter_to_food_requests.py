"""added shelter to food requests

Revision ID: b0eab0c78c43
Revises: 877c30f435a5
Create Date: 2021-05-13 20:36:38.567637

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b0eab0c78c43'
down_revision = '877c30f435a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('food_requests', sa.Column('shelter', sa.String(length=254), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('food_requests', 'shelter')
    # ### end Alembic commands ###