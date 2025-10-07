<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="Ex1"/>
        <attribute name="authors" value="A"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-17 09:05:31 PM"/>
        <attribute name="created" value="QTtOQVRUQVBPTkdQQzsyMDI1LTA3LTE3OzA5OjAwOjU2IFBNOzIxODQ="/>
        <attribute name="edited" value="QTtOQVRUQVBPTkdQQzsyMDI1LTA3LTE3OzA5OjA1OjMxIFBNOzI7MjI5MQ=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="startnum, endnum" type="Integer" array="False" size=""/>
            <assign variable="startnum" expression="0"/>
            <assign variable="endnum" expression="0"/>
            <output expression="&quot;Input start number: &quot;" newline="True"/>
            <input variable="startnum"/>
            <output expression="&quot;Input end number: &quot;" newline="True"/>
            <input variable="endnum"/>
            <while expression="startnum&lt;=endnum">
                <output expression="startnum" newline="True"/>
                <assign variable="startnum" expression="startnum + 1"/>
            </while>
        </body>
    </function>
</flowgorithm>