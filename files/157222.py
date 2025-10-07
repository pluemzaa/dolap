<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="test1"/>
        <attribute name="authors" value="ZXN"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-16 07:40:18 PM"/>
        <attribute name="created" value="WlhOO0xBUFRPUC0yOVVSOFUyVTsyNTY4LTA3LTE2OzA3OjM0OjQ5IFBNOzI2MjE="/>
        <attribute name="edited" value="WlhOO0xBUFRPUC0yOVVSOFUyVTsyNTY4LTA3LTE2OzA3OjQwOjE4IFBNOzI7MjcyMw=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="Start, End" type="Integer" array="False" size=""/>
            <output expression="&quot;input start number:&quot;" newline="True"/>
            <input variable="Start"/>
            <output expression="&quot;input end number:&quot;" newline="True"/>
            <input variable="End"/>
            <while expression="Start&lt;(End+1)">
                <output expression="Start" newline="True"/>
                <assign variable="Start" expression="Start+1"/>
            </while>
        </body>
    </function>
</flowgorithm>