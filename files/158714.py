<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4.3"/>
        <attribute name="authors" value="LENOVO"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-22 09:07:35 PM"/>
        <attribute name="created" value="TEVOT1ZPO0xBUFRPUC1BR01TQlYzVDsyNTY4LTA3LTIyOzA5OjA0OjIyIFBNOzI4NTI="/>
        <attribute name="edited" value="TEVOT1ZPO0xBUFRPUC1BR01TQlYzVDsyNTY4LTA3LTIyOzA5OjA3OjM1IFBNOzE7Mjk2Nw=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="i, n" type="Integer" array="False" size=""/>
            <output expression="&quot; Input start number: &quot;" newline="True"/>
            <input variable="i"/>
            <output expression="&quot; Input end number: &quot;" newline="True"/>
            <input variable="n"/>
            <while expression="i&lt;=n">
                <output expression="i" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>