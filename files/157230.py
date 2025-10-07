<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="1"/>
        <attribute name="authors" value="tanapat"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 08:40:48 PM"/>
        <attribute name="created" value="dGFuYXBhdDtUQU5BUEFULVVCVU5UVTsyMDI1LTA3LTE2OzA4OjIxOjA1IFBNOzMwNzc="/>
        <attribute name="edited" value="dGFuYXBhdDtUQU5BUEFULVVCVU5UVTsyMDI1LTA3LTE2OzA4OjQwOjQ4IFBNOzE7MzE5Mw=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="start, end, i, n" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number: &quot;" newline="True"/>
            <input variable="start"/>
            <output expression="&quot;Input end number: &quot;" newline="True"/>
            <input variable="end"/>
            <assign variable="i" expression="1"/>
            <while expression="start &lt;= end">
                <output expression="start" newline="True"/>
                <assign variable="start" expression="start + i"/>
            </while>
        </body>
    </function>
</flowgorithm>